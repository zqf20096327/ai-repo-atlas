# DuarteSantos8/schnaeppli

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/DuarteSantos8/schnaeppli) · 个人维护

**自托管 AI 购物代理：盯市场为你找划算货**

自托管的购物代理应用：用户用自然语言描述想买的商品，系统将其转为结构化搜索（含替代品、排除词、预算），按计划从已启用的市场源收集新列表，先用规则免费过滤，再调用用户配置的 AI 提供商分析商品状况并估算市场价，用纯代码从 0 到 100 打分，通过 Telegram 推送通知。提供可安装 PWA 界面。要求 Docker Compose v2、带 TLS 的反向代理与 AI API key，仅建议在私有网络运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言搜索转为结构化查询，AI 填写字段可人工编辑确认
- Deal Score 用纯代码计算并逐项解释，区分卖家陈述与 AI 假设
- 支持 vision 模型照片检查与 AI 成本跟踪、限额与自动暂停
- 仅使用官方 API 与允许的访问方式，不绕过反爬保护

## 适用场景

- 长期盯瑞士本地二手市场找特定型号相机等划算货
- 自建服务管理多个独立搜索与预算
- 通过 Telegram 接收异常低价与降价提醒

## 场景标签

`AI 助手` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3:  A self-hosted AI shopping agent.
> L26: Schnäppli turns that into a structured search (products, sensible alternatives with a reason for each, exclusions, 
> L32: 3. **Analyses** the rest with your AI provider: what the item really is, its condition, what's included, red flags,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `150fec3bc06a` · [字段定义](../../DATASET.md)*
