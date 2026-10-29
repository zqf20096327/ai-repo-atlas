# fairdataihub/alt-text-generator

⭐ 38 · Python · MIT · 推送 2026-01-24 · [GitHub](https://github.com/fairdataihub/alt-text-generator) · [官网](https://alt.fairdataihub.org) · 组织维护

**Flask REST 服务：为图片 URL 生成无障碍替代文本**

基于 Flask 的轻量 REST API，接收图片 URL 后流式下载图片，经 SSRF 校验与格式/大小限制，转 base64 发送给 Ollama 的 qwen3-vl:4b 视觉语言模型，返回一句话 alt 文本；支持自定义 prompt。Python 依赖仅 Flask 与 Requests，模型推理依赖外部 Ollama 服务，可通过环境变量配置模型与端口。提供 /health、/up 健康检查端点，附 Docker Compose 部署配置（GPU 支持）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接收图片 URL 生成替代文本的 REST API，支持自定义 prompt
- 推理由 Ollama（qwen3-vl:4b）完成，Python 依赖仅 Flask/Requests
- 内置 SSRF 防护、URL/Content-Type 校验与 10 MiB 大小限制
- 提供 /health、/up 健康检查端点与 Docker Compose 部署

## 适用场景

- 为网站图片批量生成无障碍替代文本
- 接入内容管理系统自动补充 alt 属性
- 在已有 Ollama 服务上快速部署图像描述 API

## 场景标签

 · 领域:图像理解/Web 服务

## 证据(README 行号)

> L5: A Flask-based REST API that generates accessible alt text descriptions for images using vision-language models. The 

## 星数曲线

```mermaid
xychart-beta
    title "fairdataihub/alt-text-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0588d7c7203f` · [字段定义](../../DATASET.md)*
