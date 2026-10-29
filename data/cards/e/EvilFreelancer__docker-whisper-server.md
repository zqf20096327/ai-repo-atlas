# EvilFreelancer/docker-whisper-server

⭐ 30 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/EvilFreelancer/docker-whisper-server) · 个人维护 · 中文 README

**whisper.cpp 语音转录服务的 Docker 化 OpenAI 兼容 API 网关**

将 whisper.cpp HTTP server 封装为 Docker 镜像，并提供一个独立的路由服务器：通过 config.yml 声明多个模型与多个后端端点，请求时随机或按 GPU 负载选择服务器转发，对外暴露 OpenAI 兼容的 /audio/transcriptions、/audio/translations、/models 等端点，可直接被 OpenAI 客户端调用。支持模型量化参数（q2_k 至 q8_0）与多语言指定，另有 Intel Arc 镜像与 Swagger 文档服务。要求 Nvidia GPU（GTX 10xx 以上）、CUDA 12.5+、Docker 与 Nvidia Docker Runtime。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容的转写/翻译/模型列表 API 端点
- config.yml 配置多模型多端点，按随机或 GPU 负载路由请求
- 两阶段 CUDA Docker 构建（devel 编译 + runtime 运行），支持模型量化选项
- 提供 Intel Arc 镜像与 Swagger UI 文档服务

## 适用场景

- 用 Docker 自建兼容 OpenAI 客户端的语音转录 API 服务
- 多容器、多 GPU 环境下分发转录请求
- 在本地网络为应用提供 ASR 接口并查阅 API 文档

## 场景标签

`语音识别` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L5: Whisper.cpp HTTP-сервер для автоматического распознавания речи (ASR), предоставляющий API, совместимое с
> L208: В конфигурации можно указать несколько моделей и серверов для каждой модели, в случае если модель доступна на неск
> L241: curl http://localhost:5000/audio/transcriptions \

## 星数曲线

```mermaid
xychart-beta
    title "EvilFreelancer/docker-whisper-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8125cb85d00f` · [字段定义](../../DATASET.md)*
