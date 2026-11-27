# SenjuWoo/Ultimate-AI-Starter-Bundle

⭐ 10 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/SenjuWoo/Ultimate-AI-Starter-Bundle) · [官网](https://github.com/SenjuWoo/Ultimate-AI-Starter-Bundle/releases) · 个人维护

**一个 Windows 安装器，让六个 AI 编码应用共享同一套技能与工具**

面向 Windows 的安装包，将 81 个通用技能、基础 MCP（context7/headroom/toolbox 等）以各应用自有格式写入 Claude Code、Codex、Grok、Kimi、Hermes、Google Antigravity 六个 AI 编码应用；技能按需加载，MCP 默认停驻。附带编译器套件安装、安装状态自检 doctor、`PLAN.md`/`STATE.md` 项目模板与无模型调用的任务控制器。Forge 类游戏模组工具作为独立 add-on 仅被发现与注册，不重复安装。升级保留用户模型选择与配置，无静默回退链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一套 81 个技能按各应用自有格式写入六个 AI 编码应用，技能按需加载
- 安装末步运行 installed-state doctor，PASS 需命令实际执行并校验退出码
- 提供本地模型与免费档路由选项，发布前双重构建并要求字节一致
- Forge/伴生工具通过 uabs-companion.json 自注册，独立维护与安装

## 适用场景

- 在多台 Windows 机器上为多个 AI 编码应用统一配置技能与 MCP
- 新开项目时用 PLAN/STATE 模板与任务控制器管理任务交接
- 按预算刷新提供商路由，选用最便宜的缓存读取通道

## 场景标签

 · 领域:AI 开发工具链/开发环境配置

## 证据(README 行号)

> L14: One installer that gives every AI coding app on Windows the same skills, tools and
> L22: **What it is not:** another model, a hosted service, or a package manager for
> L46: Claude Code · Codex · Grok · Kimi · Hermes · Google Antigravity. Each gets the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `ef720f8a24b9` · [字段定义](../../DATASET.md)*
