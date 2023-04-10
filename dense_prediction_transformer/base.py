import torch


class BaseModel(torch.nn.Module):
    def load(self, path):
        """Load model from file. If optimizer parameters are present, load them as well.

        Args:
            path (str): file path
        """
        parameters = torch.load(path, map_location=torch.device("cpu")) # load parameters from file

        # Check if optimizer parameters are present
        if "optimizer" in parameters:
            parameters = parameters["model"] # get model parameters

        self.load_state_dict(parameters) # load model parameters
