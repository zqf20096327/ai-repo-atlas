# AsuraAce/ambit

⭐ 47 · TypeScript · GPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/AsuraAce/ambit) · 个人维护

**本地优先的 AI 生成图片库桌面管理应用**

面向持有大量 AI 生成图片的用户，Ambit 是 Windows 桌面应用（Tauri + Rust + React 19 + SQLite）：导入文件夹编目而不移动源文件，解析 prompt、workflow、模型引用等生成元数据，支持按元数据搜索、收藏集、时间线浏览、视频库管理与 ComfyUI 视频元数据查看。本地运行为默认，无遥测；Gemini 驱动的提示词恢复等为可选功能，需自配 key 才启用。公测版仅提供 Windows 安装包，macOS/Linux 尚在验证，macOS/Linux 构建需 Node.js 24+、pnpm、Rust。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 解析 prompt/workflow/模型哈希等生成元数据并支持搜索过滤
- 编目不移动源文件，SQLite 支持大规模库的快速查询
- 本地运行为默认、无遥测，Gemini 功能需自配 key 显式启用
- 支持视频库导入与 ComfyUI 视频元数据查看

## 适用场景

- 整理和检索大量 AI 生成图片与生成参数
- 通过模型哈希在线解析（可选）确认模型来源
- 在本地离线浏览、维护图片库而不上传数据

## 场景标签

 · 领域:桌面工具/图片管理

## 证据(README 行号)

> L6: Ambit is a local-first desktop app for organizing large AI-generated image libraries. It helps you import folders, b
> L27: * **Optional intelligence tools**: Gemini-backed actions are available only when you configure your own key and exp

## 星数曲线

```mermaid
xychart-beta
    title "AsuraAce/ambit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-29 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8ab4de0c8f1c` · [字段定义](../../DATASET.md)*
