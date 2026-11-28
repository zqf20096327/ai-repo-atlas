# rsxdalv/TTS-WebUI

⭐ 3,317 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/rsxdalv/TTS-WebUI) · [官网](http://TTSWebUI.com/) · 个人维护

**整合多款语音/音频生成模型的 Gradio + React WebUI**

以 Gradio 为后端、React 为前端的本地网页界面，将数十个语音合成、音乐/音频生成与音频转换模型集成到统一入口，按文本转语音、音频/音乐生成、音频转换工具三类组织。模型分基础安装与扩展两类，扩展以 pip 包形式从界面或启动器安装。提供 Windows 安装器、手动安装与 Docker 部署路径，并通过 OpenAI 兼容 API 接入 SillyTavern、OpenWebUI 等客户端。基础安装约 10.7 GB，部分依赖为非宽松许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三类音频任务（TTS/音乐生成/音频转换）统一到单一 WebUI
- 数十个模型可作扩展安装，支持从界面、启动器或 JSON 安装器添加
- 提供 OpenAI 兼容 TTS API 端点，可接入 SillyTavern、OpenWebUI
- 支持 winget 安装器、手动安装与 Docker（含 CUDA 容器说明）

## 适用场景

- 在本地网页界面中试用和对比多种 TTS 与音乐生成模型
- 为 SillyTavern 或 OpenWebUI 配置本地语音合成 API
- 用 RVC、Demucs 等工具做声音转换与音频处理

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L37: ## Supported Models
> L69: \* These models are not installed by default, instead they are available as extensions.
> L88: * Run start_tts_webui.bat or start_tts_webui.sh to start the server. It will ask you to select the GPU/Chip you are

## 星数曲线

```mermaid
xychart-beta
    title "rsxdalv/TTS-WebUI 星数(近 20 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 3291 --> 3320
    line [3295, 3293, 3295, 3296, 3297, 3299, 3300, 3294, 3309, 3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3317, 3318, 3317]
```

2026-10-26 3,295 → 2026-11-28 3,317（+22）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `02cd0bd57f2a` · [字段定义](../../DATASET.md)*
