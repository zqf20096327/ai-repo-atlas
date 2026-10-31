# cdzombak/lychee-ai-organizer

⭐ 13 · Go · GPL-3.0 · 推送 2026-04-23 · [GitHub](https://github.com/cdzombak/lychee-ai-organizer) · 个人维护

**用本地 LLM 整理 Lychee 相册中未分类照片的 Web 应用**

面向 Lychee 自托管相册用户的照片整理工具：读取 Lychee 数据库（MySQL/PostgreSQL/SQLite），调用 AI 模型为照片和相册生成描述，并在 Web 界面中为每张未分类照片推荐三个相册。支持 Ollama 本地模型（推荐 qwen2.5vl:3b 做图像分析、qwen3:8b 做描述合成）或任意 OpenAI 兼容 API。需先在数据库手动添加 AI 描述列。仅限本地个人使用，无身份认证。以 Homebrew/apt 包、预编译二进制、Docker 镜像及源码构建方式分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 生成照片与相册描述，为未分类照片推荐相册
- 支持 Ollama 本地模型与 OpenAI 兼容 API 双后端
- 提供 Homebrew/apt/预编译二进制/Docker 多种分发方式
- 提供 REST API 与 WebSocket 实时进度

## 适用场景

- 把 Lychee 里堆积的未分类照片归入相册
- 用本地 Ollama 模型为照片生成描述以保护隐私
- 批量处理自托管相册的照片整理

## 场景标签

`多模态` `推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L3: This application helps organize an existing Lychee photo library into albums using artificial intelligence. It conne
> L6: - **Ollama**: Local, open-source AI models (recommended for privacy and cost)

## 星数曲线

```mermaid
xychart-beta
    title "cdzombak/lychee-ai-organizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0dc700c82c44` · [字段定义](../../DATASET.md)*
