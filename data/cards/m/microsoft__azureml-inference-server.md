# microsoft/azureml-inference-server

⭐ 28 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/microsoft/azureml-inference-server) · 组织维护

**微软 AzureML 的推理 HTTP 服务器包，将模型暴露为 HTTP 端点**

azureml-inference-server-http Python 包封装了基于 Flask 或 Sanic 的 HTTP 服务器代码及依赖，用于接收推理请求并运行用户提供代码与已部署模型交互。该服务器默认包含在 Azure ML 预构建推理 Docker 镜像中，是基础镜像的主要组件。开发者可克隆仓库后用 pip 以可编辑模式安装并验证 azmlinfsrv 命令。README 仅给出源码安装步骤，详细文档链接未在本页展开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将机器学习模型暴露为 HTTP 端点的服务器组件
- Flask 或 Sanic 服务器代码打包为单一 Python 包
- 默认包含于 Azure ML 预构建推理 Docker 镜像

## 适用场景

- 部署 Azure ML 模型时提供推理 HTTP 服务
- 本地开发调试推理服务器代码

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: The HTTP server is the component that facilitates inferencing to deployed models. Requests made to the HTTP server r
> L4: This server is used with most images in the Azure ML ecosystem, and is considered the primary component of the base 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/azureml-inference-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cf1f115aebfb` · [字段定义](../../DATASET.md)*
