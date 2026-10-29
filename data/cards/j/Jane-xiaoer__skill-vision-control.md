# Jane-xiaoer/skill-vision-control

⭐ 66 · TypeScript · MIT · 推送 2026-04-21 · [GitHub](https://github.com/Jane-xiaoer/skill-vision-control) · 个人维护 · 中文 README

**MCP Skill 版本管理器：检测更新、安全扫描与智能合并**

面向使用 Claude/MCP 技能的开发者的命令行版本管理工具：从 GitHub 或 npm 来源注册技能，自动检测新版本、下载前执行基于 Sentinel 模式的安全扫描（eval/exec 等高风险代码识别），保留多版本并支持随时切换、回滚、A/B 测试与定时检查。支持 fork 自定义分支，将官方更新与本地修改智能合并并处理冲突。同时可作为 MCP Server 运行，暴露 9 个工具供 AI 调用管理技能。以 npm 全局安装方式提供，数据存储于 ~/.svc/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 GitHub/npm 来源注册技能并检测版本更新
- 下载前自动安全扫描，按 CRITICAL/SUSPICIOUS/WARNING 分级
- 多版本保留、切换、回滚与 A/B 测试
- fork 分支后可将官方更新与自定义修改智能合并

## 适用场景

- 管理多个 MCP 技能的版本更新与回滚
- 安装第三方技能前先做安全扫描
- 在自定义修改的基础上合并官方更新
- 让 AI 通过 MCP 接口代为管理技能版本

## 场景标签

 · 领域:AI 工具链/版本管理

## 证据(README 行号)

> L6: > **Safe MCP Skill Version Manager** - Detect updates, parallel testing, smart merge, confirm before replace
> L17: - 🤖 **MCP Server** - Let AI manage your skills
> L121: ## Using as MCP Server

## 星数曲线

```mermaid
xychart-beta
    title "Jane-xiaoer/skill-vision-control 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-29 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f3a067dffd81` · [字段定义](../../DATASET.md)*
