# TextGeneratorio/text-generator.io

⭐ 38 · Python · 推送 2026-10-27 · [GitHub](https://github.com/TextGeneratorio/text-generator.io) · [官网](https://text-generator.io) · 组织维护

**可自托管的多模型 AI API 服务：文本生成、TTS 与语音转写**

text-generator.io 的服务端系统：在磁盘、RAM 与 GPU 间平衡调度多个模型，通过换入 AI 网络对外提供 API；支持文本与语音生成、基于 NVIDIA Parakeet 的语音转写，以及用 OCR、网页抓取、图像描述做提示数据增强。API 与 OpenAI 兼容（尚不支持 ChatGPT API），提供按概率早停、限制句数等生成控制。可通过云 API 使用或自行托管（Docker/Kubernetes），模型权重从 HuggingFace 下载；无 Docker 路径需安装 ffmpeg、tesseract-ocr 等系统依赖，使用 PostgreSQL 做用户认证与文档存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型在磁盘/RAM/GPU 间的平衡调度与按需换入
- OpenAI 兼容 API，附文本转写、语音生成路由
- 链接/图像提示增强：抓取摘要、图像描述与 OCR
- 提供 Docker 镜像下载脚本与 Kubernetes 部署配置

## 适用场景

- 自托管一套文本生成加语音转写/合成的 API 服务
- 用 OpenAI 兼容接口接入现有客户端做文本生成
- 对含链接与图像的提示自动做数据富化

## 场景标签

`推理引擎` `语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L5: Text Generator is a system for;
> L7: * Serving AI APIs via swapping in AI Networks.
> L36: Text Generator is API compatible with OpenAI (but not the ChatGPT API yet)

## 星数曲线

```mermaid
xychart-beta
    title "TextGeneratorio/text-generator.io 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0208e9c19b34` · [字段定义](../../DATASET.md)*
