# alvertogit/deeplearning_flask

⭐ 21 · Jupyter Notebook · 推送 2026-10-25 · [GitHub](https://github.com/alvertogit/deeplearning_flask) · 个人维护

**用 Flask 将 MNIST 深度学习模型部署为微服务的演示项目**

演示型仓库：在 Jupyter Lab 中用 Keras/TensorFlow 定义并训练 MNIST 手写数字识别模型，再通过 Flask + Gunicorn 部署为 REST API 微服务，客户端上传图片即可返回预测标签。架构采用 Docker Compose 两容器（NGINX 反向代理 + Flask/Gunicorn），CI/CD 由 GitHub Actions 执行 pytest 测试，代码用 Ruff 检查，依赖管理基于 uv。作者定位为技能测试（test to demonstrate skills），非通用产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Keras/TensorFlow 训练 MNIST 模型并经 REST API 返回预测
- Docker Compose 双容器架构（NGINX + Flask/Gunicorn）
- GitHub Actions CI/CD 自动运行 pytest 测试
- uv 管理依赖，Ruff 做 lint 与格式化

## 适用场景

- 学习如何把深度学习模型部署为 REST 微服务
- 参考 Docker Compose + NGINX + Gunicorn 的服务架构
- 作为 GitHub Actions CI/CD 的示例工程

## 场景标签

`推理引擎` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L9: The goal is to deploy on [Flask] a [Deep Learning] model as a microservice. The model is used to predict handwritten
> L127: ~/deeplearning_flask$ curl -F file=@app/app/static/4.jpg -X POST 'http://127.0.0.1/api/predictlabel' | json_pp

## 星数曲线

```mermaid
xychart-beta
    title "alvertogit/deeplearning_flask 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ab340d2ad2a0` · [字段定义](../../DATASET.md)*
