# spaceman2408/CharacterVault

⭐ 23 · TypeScript · GPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/spaceman2408/CharacterVault) · [官网](https://charactervault.app/) · 个人维护

**浏览器内的 V2/V3 角色扮演角色卡与世界书编辑器**

纯前端 Web 应用：提供覆盖全部 V2/V3 字段的角色卡编辑器、SillyTavern 格式世界书编辑器（含递归解锁关系图）、素材库网格管理、PNG/JSON 导入导出、快照与 ZIP 备份，数据仅存于浏览器 IndexedDB，无需服务器与账号。AI 功能为可选的 bring-your-own-key 模式：聊天助手 Orion、代写角色卡/世界书的 AI Agent（落地前可审 diff）、文本增强工具栏与从概念生成整卡的 Creation Studio，可配置任意 OpenAI 兼容端点。可在线使用、本地 npm 运行或 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整 V2/V3 角色卡与 SillyTavern 世界书编辑，含递归关系图
- AI 功能全部可选，BYOK 接任意 OpenAI 兼容端点，无自有 AI 服务器
- 数据仅存浏览器 IndexedDB，支持快照对比与 ZIP 备份恢复
- 提供 SillyTavern 伴侣扩展，可从 SillyTavern 直接发送卡片

## 适用场景

- 为 SillyTavern 等前端创建和管理角色卡与世界书
- 让 AI Agent 代写角色卡，审阅 diff 后再应用
- 本地或 Docker 私有部署，浏览器内离线整理角色库

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3:  Create, edit, and organize roleplay character cards and lorebooks in your browser
> L58: Every AI feature is optional. The editor, lorebooks, import, export, and snapshots all work without it.

## 星数曲线

```mermaid
xychart-beta
    title "spaceman2408/CharacterVault 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-26", "2026-10-28"]
    y-axis "stars" 19 --> 24
    line [20, 21, 22, 23, 23]
```

2026-10-18 20 → 2026-10-28 23（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2e0d6350f971` · [字段定义](../../DATASET.md)*
