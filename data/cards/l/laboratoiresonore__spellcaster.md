# laboratoiresonore/spellcaster

⭐ 60 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/laboratoiresonore/spellcaster) · 个人维护

**面向 GIMP/Darktable/Resolve 的本地 AI 图像视频生成插件套件（75 工具）**

为 GIMP 3、DaVinci Resolve、Darktable 提供插件、另带聊天 UI（Wizard Guild）与 SillyTavern 扩展，统一连接后台 ComfyUI 完成本地 AI 生成。覆盖文生图（Flux/SDXL 等 9 个模型族）、图像到视频（Wan 2.2/LTX 2.3）、抠图、修复、上色、换脸、放大等 75 个工具，共 19 个模型。自动检测已装 checkpoint 并路由到对应架构。安装需 ComfyUI、GIMP 3 与 4GB+ VRAM 的 GPU，提供 Windows/macOS/Linux 安装包、通用安装脚本与远程 ComfyUI 场景的 Remote Installer；Resolve 插件仍处测试阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 75 个 AI 工具接入 GIMP/Darktable/Resolve/聊天 UI/SillyTavern，共享同一 ComfyUI 后端与画廊
- 自动检测已安装 checkpoint 并按架构路由生成任务
- 提供自更新安装器、健康检查器与远程 ComfyUI 的 Remote Installer
- 支持文生图、图生视频、AI 选择（SAM 3）、修复、上色、换脸、放大等功能

## 适用场景

- 在 GIMP 中直接用文字描述完成选区、修复、擦除、上色等操作
- 把静态图转为视频片段并送入 DaVinci Resolve 时间线
- 在无 GPU 的笔记本上通过局域网调用另一台机器上的 ComfyUI
- 在 Darktable 中对整组 RAW 照片批量执行 AI 处理

## 场景标签

`图像生成` `视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L6:  75 AI tools, one menu. GIMP · DaVinci Resolve · Darktable · chat UI · 100% local · zero config.
> L65:  🎨 Image &nbsp;<code>Flux 2 Klein</code> · <code>Flux 1 Dev</code> · <code>Flux Kontext</code> · <code>Chroma</code
> L123:  Icon key · 🖌️ GIMP plugin · 📷 Darktable plugin · 🧙 Wizard Guild chat · 🎬 DaVinci Resolve plugin · 🎭 SillyTavern e

## 星数曲线

```mermaid
xychart-beta
    title "laboratoiresonore/spellcaster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-24 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `31ec9269a5ea` · [字段定义](../../DATASET.md)*
