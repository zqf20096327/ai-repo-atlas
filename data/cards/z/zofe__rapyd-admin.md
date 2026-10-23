# zofe/rapyd-admin

⭐ 862 · PHP · MIT · 推送 2026-10-20 · [GitHub](https://github.com/zofe/rapyd-admin) · 个人维护

**面向 Laravel 的轻量管理面板，适配 AI agent 协作开发**

基于 Livewire + Blade 的 Laravel 开源管理面板，以 Nova、Filament、Backpack 的轻量替代为定位。生成器把普通 Livewire 组件与 Blade 视图写入 app/Modules，可直接编辑；内置认证（Fortify + Socialite、2FA）、角色权限、1–3 层多租户 Companies、工作流与日志查看器。面向构建 SaaS 的团队与 AI agent 开发场景：提供 rpd:context 生成 agent 简报、写入 AGENTS.md/CLAUDE.md 与 .claude/skills，日志查看器含 AI 错误分析。要求 PHP 8.2+、Laravel 12/13、Livewire 4，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成器输出普通 Livewire 组件与 Blade 视图到 app/Modules，无 DSL
- 内置认证、2FA、Google 登录、角色权限与多租户 Companies
- rpd:context 与 rpd:ai 为 AI agent 提供简报、指导文件与技能
- 模块可通过 composer 包扩展（shop/payments/ai 模块），模块可 eject 深度修改

## 适用场景

- 快速搭建带认证与多租户的 SaaS 后台
- 让 AI agent 按规范生成和修改管理模块
- 用两条命令生成带表格、详情页和表单的业务模块

## 场景标签

 · 领域:Web 开发/管理面板

## 证据(README 行号)

> L9: **Rapyd Admin** is an open-source admin panel for Laravel: a light alternative to Nova, Filament and Backpack for te
> L113: ## Working with AI agents
> L126: The package itself is developed this way: see docs/AI.md for the agent brief, the AI error analysis in

## 星数曲线

```mermaid
xychart-beta
    title "zofe/rapyd-admin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 861 --> 863
    line [862, 862]
```

2026-10-18 862 → 2026-10-23 862（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cf413ef1c222` · [字段定义](../../DATASET.md)*
