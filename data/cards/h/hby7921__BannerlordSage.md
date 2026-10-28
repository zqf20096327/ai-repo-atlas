# hby7921/BannerlordSage

⭐ 22 · TypeScript · MIT · 推送 2026-10-09 · [GitHub](https://github.com/hby7921/BannerlordSage) · 个人维护 · 中文 README

**为《骑马与砍杀2》Mod 开发者提供 MCP 服务器：源码/XML 检索与补丁生成**

面向 Mount & Blade II: Bannerlord Mod 开发与逆向工程的 MCP 服务器：读取本地游戏安装，导入 XML、用 ILSpyCmd 反编译官方 DLL，构建 SQLite 索引，向 AI 编码 agent 暴露 43 个工具，覆盖官方源码全文检索、C# 类型读取、本地化解析、结构化玩法查询（兵种树/装备/英雄/王国）、本地 Mod 源码索引、Harmony/XSLT 补丁脚手架生成、项目记忆与实验性编辑器工具。运行需 Windows、本地正版游戏、Bun、ripgrep、.NET SDK 8+ 与 ILSpyCmd；编辑器功能为实验版本且部分能力未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 43 个 MCP 工具，分默认/完整两个入口
- 反编译官方 DLL 并建 SQLite 索引，支持全文源码检索与 XML 查询
- Harmony 补丁、XSLT 补丁模板与 Mod 工程结构生成
- 项目记忆工具：存储/检索决策、坑点与偏好

## 适用场景

- 让 AI 编码 agent 检索游戏反编译源码以开发 Mod
- 查询游戏内兵种树、装备、英雄等结构化数据
- 为已有 Mod 建立本地源码索引供 agent 阅读
- 跨会话保存与恢复 Mod 项目的工作记忆

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: An MCP server for **Mount & Blade II: Bannerlord** that provides source code search and data browsing.
> L13: It reads your local Bannerlord installation, imports XML, decompiles official DLLs, builds a SQLite index, and expo
> L36: BannerlordSage provides **43 tools** across two entrypoints:

## 星数曲线

```mermaid
xychart-beta
    title "hby7921/BannerlordSage 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0ffead823a48` · [字段定义](../../DATASET.md)*
