# iceburgcrm/iceburgcrm

⭐ 228 · JavaScript · AGPL-3.0 · 推送 2026-08-28 · [GitHub](https://github.com/iceburgcrm/iceburgcrm) · [官网](https://www.iceburg.ca) · 组织维护

**元数据驱动的 Laravel CRM，可让 AI 按描述生成 CRM**

基于 Laravel 10 + Vue 3 + Inertia 的开源元数据驱动 CRM：模块、字段、关系、子面板均由元数据定义，支持动态模块、模块级多向关系、6 种格式导入导出、26 套明暗主题、角色权限、内置 API 与工作流，并可将已有数据库（如 WordPress）转为 CRM。AI 为可选能力：用自然语言描述需求由 AI（默认 ChatGPT 3.5，Dalle-3 生成登录页图像）自动生成 CRM 定义；另提供 AI Assist 按钮为空字段建议取值，需配置 OpenAI/OpenRouter/Claude API key。提供 composer 快速安装与 Docker 方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 元数据定义模块/字段/关系/子面板，支持自定义 CRM 原型
- AI Builder：描述需求后由 AI 生成 CRM（含登录页图像生成）
- AI Assist 为空字段提供 AI 建议值，保存前有确认预览
- 支持 OpenAI / OpenRouter / Claude 多个 AI 提供方配置

## 适用场景

- 快速搭建默认 55 模块的企业 CRM 或按需定制原型
- 把已有数据库（如 WordPress 站点）转成管理面板/CRM
- 让 AI 根据一句话描述自动生成特定领域的 CRM

## 场景标签

 · 领域:企业管理软件/CRM

## 证据(README 行号)

> L3: #### With optional AI Assist, AI Builder
> L41: Iceburg CRM is a metadata driven CRM with AI abilities that allows you to quickly prototype any CRM. The default CR
> L149: ## AI Assist (Optional)

## 星数曲线

```mermaid
xychart-beta
    title "iceburgcrm/iceburgcrm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 227 --> 229
    line [228, 228]
```

2026-10-18 228 → 2026-10-22 228（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9325807b1278` · [字段定义](../../DATASET.md)*
