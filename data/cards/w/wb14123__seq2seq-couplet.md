# wb14123/seq2seq-couplet

⭐ 5,474 · Python · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/wb14123/seq2seq-couplet) · [官网](https://ai.binwang.me/couplet) · 个人维护 · 中文 README

**用 seq2seq 深度学习模型生成对联的项目**

基于 TensorFlow 的 seq2seq 模型项目，用户输入上联可生成对应下联。提供训练脚本 couplet.py（可在 TensorBoard 查看损失与 bleu 分数、支持断点续训）与 server.py 启动的 Web 服务，另可构建 Docker 镜像部署。运行需自备数据集（作者提供下载），作者在 GTX-1080 GPU 上训练约 4 天。提供在线演示页面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- seq2seq 模型根据上联生成下联
- 提供训练脚本，支持断点恢复继续训练
- server.py 启动 Web 服务对联
- 支持 Docker 镜像部署

## 适用场景

- 在线体验 AI 对对联
- 自行训练/微调 seq2seq 模型
- 部署对联生成 Web 服务

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L1: This is a project use seq2seq model to play couplets (对对联)。 This project is written with Tensorflow. You can try the
> L19: Open `couplet.py` and config the file locations and hyperparams. Then run `python couplet.py` to train the model. Y
> L29: Open `server.py` and config the `vocab_file` and `model_dir` params. Then run `python server.py` will start a web s


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `23e03ced3a27` · [字段定义](../../DATASET.md)*
