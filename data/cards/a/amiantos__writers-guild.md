# amiantos/writers-guild

⭐ 14 · JavaScript · MPL-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/amiantos/writers-guild) · 个人维护

**面向短篇小说写作的自托管 AI 应用，兼容 Tavern 角色卡**

自托管的 AI 互动写作 Web 应用：导入 Tavern V2 角色卡（PNG/CHUB）与 SillyTavern 世界书，以内置激活引擎和 ST 宏（{{random}}/{{pick}}）驱动短篇/小说体裁的续写，强制统一第三人称过去时视角，并可自动改写角色开场白。支持从特定角色视角续写、开放式生成、指定事件生成，实验性多人聊天功能可选。需配置 DeepSeek API key；支持多用户邀请与各自独立库。提供 npm 源码运行与 Docker 多架构镜像部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 导入 Tavern V2 角色卡与 SillyTavern 世界书（含激活引擎）
- 支持 ST 宏与视角/时态一致性自动改写
- 实验性聊天功能与可选多用户系统（每人独立库）
- Docker 多架构镜像（amd64/arm64）发布

## 适用场景

- 用现有角色卡和世界书进行短篇小说式 AI 创作
- 多角色互动叙事并指定事件走向
- 自托管并与朋友分享，各人拥有私有角色/故事库

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: AI-powered short story writing application that supports Tavern character cards and SillyTavern lorebooks.
> L128: 2. Navigate to Settings and add your DeepSeek API key

## 星数曲线

```mermaid
xychart-beta
    title "amiantos/writers-guild 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4e8accd1c537` · [字段定义](../../DATASET.md)*
