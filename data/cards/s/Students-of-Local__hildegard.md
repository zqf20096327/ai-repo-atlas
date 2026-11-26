# Students-of-Local/hildegard

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/Students-of-Local/hildegard) · [官网](https://dbaney.com/hildegard/) · 组织维护

**自有 GPU 上的本地 AI 创作工作室：视频、语音、角色、3D**

在本地 GPU 上运行的开源 AI 创作工作室，通过 ComfyUI 驱动 LTX-2.5、LTX-2、Wan 2.2 等开放视频模型，用镜头、焦距、光圈、运镜等电影语言生成影片；语音功能覆盖语音合成、音色设计、经同意的克隆、配音与转录，并支持跨镜头保持同一面孔服装的角色。以 MCP 服务器形式接入 Claude Code、ChatGPT 等 AI 应用代为指挥出片。安装器自动为显存挑选模型；Apple silicon 与无 GPU 机器暂无模型可选。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 ComfyUI 驱动 LTX-2.5/LTX-2/Wan 2.2 开放视频模型，支持镜头与运镜预设
- 语音合成、音色设计、经同意的克隆、配音与转录（带水印）
- MCP 服务器：Claude Code、ChatGPT、Cursor 等 AI 应用可在你的 GPU 上指挥出片
- 按 GPU 显存（12/24 GB 档位）自动选择模型，全离线渲染

## 适用场景

- 在自己电脑上离线生成短片、语音与角色素材
- 让 Claude Code 等 AI 客户端通过 MCP 调度本地 GPU 出片
- 多台电脑经 Tailscale 组成渲染集群
- 给手机和朋友分享一个可访问的工作室链接

## 场景标签

`语音合成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: ### Your own AI studio, on your own GPU.
> L24: Hildegard directs open video models (LTX-2.5, LTX-2 and Wan 2.2) through ComfyUI with real camera language: bodies,
> L210: Hildegard is an MCP server. Linked apps (Claude Code, Claude Desktop, Codex, OMP, Pi, Gemini CLI, OpenCode, Cursor


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `0f599e998604` · [字段定义](../../DATASET.md)*
