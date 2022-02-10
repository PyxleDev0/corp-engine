import raylib as rl
from corpengine2.modules import core
from corpengine2.modules.colors import WHITE

class Service(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = self._type = type(self).__name__

class GameService(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.Assets = Assets(self)
        self.Workspace = Workspace(self)
        self.EngineRenderService = EngineRenderService(self)
    
    def GetService(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            core.OpenErrorWindow(f"No service named \"{name}\".", self.parent)
    
    def _Update(self):
        self.Workspace._Update()


class Assets(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.images = {}
        self.textures = {}
    
    def GetImage(self, name: str):
        try:
            return self.images[name]
        except Exception:
            core.OpenErrorWindow(f"No such image with name \"{name}\"", self.parent.parent)
    
    def LoadImage(self, name, path):
        self.images.update({name: rl.LoadImage(str.encode(path))})

    def LoadTexture(self, name, path):
        """tip: this method returns the texture, so you won't have to use GetTexture!"""
        texture = rl.LoadTexture(str.encode(path))
        self.textures.update({name: rl.LoadTexture(str.encode(path))})
        return texture


class Workspace(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.__children = {}
    
    def GetChild(self, name):
        try:
            return self.__children[name]
        except Exception:
            return None
    
    def GetChildren(self):
        return self.__children.values()
    
    def _Update(self):
        for child in self.GetChildren():
            if child.HasComponent("ScriptComponent"):
                ScriptComponent = child.GetComponent("ScriptComponent")
                if hasattr(ScriptComponent, "Update"):
                    ScriptComponent.Update()
    
    def _AddChild(self, obj):
        self.__children.update({obj.name: obj})
        if hasattr(object, "Setup"):
            object.Setup()

class EngineRenderService(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.Workspace = self.parent.Workspace
    
    def _Render(self):
        for child in self.Workspace.GetChildren():
            if child.HasComponent("TextureComponent"):
                TextureComponent = child.GetComponent("TextureComponent")
                TransformComponent = child.GetComponent("TransformComponent")
                position = TransformComponent.position
                rotation = TransformComponent.rotation
                scale = TransformComponent.scale
                texture = TextureComponent.texture
                if texture != None:
                    rl.DrawTextureEx(texture, position, rotation, scale, WHITE)
