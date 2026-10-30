# dc-tw/ai-video-drama-platform

⭐ 16 · Python · 推送 2026-10-11 · [GitHub](https://github.com/dc-tw/ai-video-drama-platform) · 个人维护 · 中文 README

**把故事大纲转成短视频的全栈流水线后端骨架**

以 FastAPI 为应用边界、Pydantic 为 LLM 与生成层契约的后端骨架：故事大纲经 OpenAI LLM 转为三个类型化场景，交由本地 ComfyUI 逐场景生成图像，再用 FFmpeg 确定性合成 MP4，可经 CLI 一条命令完成全流程或经 API 仅生成分镜。v0.1 无浏览器前端，需自备 OpenAI API key、自行安装 ComfyUI checkpoint；character_ref 与对白目前仅为校验元数据（未接 IP-Adapter/TTS），视频工作流文件已收录但应用尚不执行。面向搭建 AI 短剧生成管线的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 故事→LLM 结构化分镜→ComfyUI 图像→FFmpeg MP4 的完整流水线
- 手动分镜模式可绕过 OpenAI，无需 API key
- 提供 Docker Compose 部署与分层测试（单元/ComfyUI/FFmpeg/E2E）
- 收录 Kandinsky 5.0 T2V 工作流文件供检视（应用未执行）

## 适用场景

- 输入一句故事大纲生成三场景短视频 MP4
- 通过 FastAPI/Swagger 检视结构化分镜生成
- 离线单测验证 LLM 边界与工作流注入逻辑

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L15: FastAPI exposes the application boundary, Pydantic is the contract between the
> L16: LLM and generation layer, ComfyUI owns local image inference, and FFmpeg owns
> L94: The `--story` value is sent to the LLM, converted into three typed scenes,

## 星数曲线

```mermaid
xychart-beta
    title "dc-tw/ai-video-drama-platform 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [16, 15, 16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bf7a4f4e6b0d` · [字段定义](../../DATASET.md)*
