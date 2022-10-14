<h1 align="center">
  <a href="https://github.com/michaelheichler/marl_evaluation_app">
    <img src="supplementary/latenightcoding_dalle.png" alt="Logo" width="125" height="125">
  </a>
</h1>

<div align="center">
  MARL Evaluation App
  <br />
  <br />
  <a href="https://github.com/michaelheichler/marl_evaluation_app/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/michaelheichler/marl_evaluation_app/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/michaelheichler/marl_evaluation_app/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

[![license](https://img.shields.io/github/license/dmichaelheichler/marl_evaluation_app.svg?style=flat-square)](LICENSE)

[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](michaelheichler/marl_evaluation_app/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![made with hearth by Michael Heichler](https://img.shields.io/badge/made%20with%20%E2%99%A5%20by-dec0dOS-ff1414.svg?style=flat-square)](https://github.com/michaelheichler/)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)  
    - [Run the environment](#run-the-environment)  
    - [Variables reference](#variables-reference)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

<table>
<tr>
<td>

Multi-Agent Reinforcement Learning Repository for my Masterthesis which reviews and supplements a couple of testing environments and displays the state-of-the-art RL for multi-agent application in cooperation with humans.

Key features of the **MARL Evaluation App**:

- Webapplication with interactive overview of the environments, agents and policys
- Different Frameworks implemented like OpenAI Gym, PettingZoo and Rllib
- Work In Progress, therefore this is a living repo which lives from feedback and input


<details open>
<summary>Additional info</summary>
<br>

This is the result of my Masterthesis about cooperation between humans and autonomous agents. A lot of research and time is gone into this project and it will be maintained. This is a topic which require further research. A entry point into this topic can be this Web-Application. Me, the dev, wishes that it will become a building block for further research.

</details>

</td>
</tr>
</table>

### Built With

- [Python](https://www.python.org)
- [OpenAI Gym](https://github.com/openai/gym)
- [Stable-baselines3](https://github.com/DLR-RM/stable-baselines3)
- [PettingZoo](https://github.com/Farama-Foundation/PettingZoo)
- [Rllib (Ray)](https://github.com/ray-project/ray/tree/master/rllib)
- [Unity Engine](https://github.com/Unity-Technologies/)
- [ML-Agents for Unity Engine](https://github.com/Unity-Technologies/ml-agents/tree/release_19_docs)

## Getting Started

### Prerequisites

First, make a new virtualenv, clone the repository

Virtualenv:
```sh
pip install virtualenv

virtualenv marl_eval_app

virtualenv activate marl_eval_app
```

Pyenv with version management:

Install Pyenv, then:
```sh
pyenv install 3.9.13

pyenv 3.9.13 marl_eval_app

pyenv shell marl_eval_app
```

The easiest way to install the required packages into the newly created virtual environment is by running:

```sh
pip install -r requirements
```

### Usage

#### Run the environment
To start up the Flask instance and the npm server (for the Flask-VUE-Bootstrap Architecture which the website is based on) run

```sh
python launch.py
```

#### Variables reference


## Roadmap

## Contributing


## Support

Reach out to the maintainer at one of the following places:

- [GitHub discussions](https://github.com/michaelheichler/marl_evaluation_app/discussions)
- The email which is located [in GitHub profile](https://github.com/michaelheichler)

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.

## Acknowledgements

Thanks for these awesome resources that were used during the development of the **Amazing GitHub template**:

- [OpenAI Gym](https://github.com/openai/gym)
- [Stable-baselines3](https://github.com/DLR-RM/stable-baselines3)
- [PettingZoo](https://github.com/Farama-Foundation/PettingZoo)
- [Rllib (Ray)](https://github.com/ray-project/ray/tree/master/rllib)
- [Unity Engine](https://github.com/Unity-Technologies/)
- [ML-Agents for Unity Engine](https://github.com/Unity-Technologies/ml-agents/tree/release_19_docs)
- <https://github.com/uoe-agents/pressureplate>
- <https://github.com/dec0dOS/amazing-github-template/blob/main/README.md>
- <https://github.com/HumanCompatibleAI/overcooked_ai>
- <https://openai.com/blog/openai-baselines-ppo/>
- <https://github.com/YuhangSong/DEHRL>
- <https://github.com/NeuralMMO/environment>
- <https://openspiel.readthedocs.io/en/latest/concepts.html>
- <https://www.kaggle.com/code/charel/learn-by-example-reinforcement-learning-with-gym>
- <https://www.gymlibrary.dev/content/basic_usage/>
- <https://becominghuman.ai/getting-mario-back-into-the-gym-setting-up-super-mario-bros-in-openais-gym-8e39a96c1e41>
- <https://python.plainenglish.io/build-an-ai-model-to-play-super-mario-7607b1ec1e17>
- <https://github.com/DavidRother/gym-cooking>
- <https://www.kaggle.com/code/koutetsu/connectx-multi-agent-reinforcement-learning-1/notebook>
- <https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/>
- <https://vuejs.org/>
- <https://github.com/mjhea0/flaskr-tdd>
- <https://holli.github.io/rusted_cart_pole/>
