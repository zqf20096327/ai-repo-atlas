# coocolab/coocolab-autoedit

⭐ 4 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/coocolab/coocolab-autoedit) · [官网](https://coocolab.com/member/resources/?slug=one-click-edit) · 组织维护 · 中文 README

**口播影片本地 AI 自动剪辑工具：剪口误、上字幕字卡**

面向口播创作者的本地自动剪辑流水线：将原片放入指定文件夹后，通过 Claude Code 或 Codex 读取 CLAUDE.md/AGENTS.md 执行剪辑流程。机制包括分段听打（mlx-whisper / faster-whisper 按硬件选择）、AI 生成待剪清单供用户确认后再剪、逐格对齐剪点、逐字字幕与 .srt 输出、重点词字卡、动态特效（MediaPipe 可选）、语速与 -14 LUFS 音量调整。全部在本地运行，无月费，影片不上传。需 Python 3.10–3.13、ffmpeg 5.1+、Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 标出重讲/卡住/语助词清单，用户确认后才剪
- 按硬件自动选择听打引擎：M 系列用 mlx-whisper、NVIDIA GPU/CPU 用 faster-whisper
- 音量对齐 -14 LUFS（YouTube/IG 标准），人声置中
- 提供 suggest.py/cut.py/fx.py 等模块供修改并接受 PR

## 适用场景

- 录口播教学片后自动剪掉讲错重讲和长停顿
- 给视频自动上逐字字幕并导出 .srt
- 在本地离线处理不想上传云端的影片素材

## 场景标签

`语音识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: 口播影片的 AI 自動剪輯工具。你照常錄，卡住、重講、停頓都沒關係，把影片丟進資料夾，跟 Claude Code 或 Codex 說一句「幫我剪這支」就好。剪片、上字幕、字卡、音量都會處理，全部在你自己的電腦上跑，免費開源。
> L23: |聽打|把人聲切成一段一段分開聽打，講到一半重講也抓得到|
> L87: |Mac（M 系列晶片）|mlx-whisper，large-v3-turbo|幾分鐘|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `dc1dd4883b80` · [字段定义](../../DATASET.md)*
