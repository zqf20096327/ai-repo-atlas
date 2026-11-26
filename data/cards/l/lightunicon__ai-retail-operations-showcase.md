# lightunicon/ai-retail-operations-showcase

⭐ 8 · 推送 2026-11-11 · [GitHub](https://github.com/lightunicon/ai-retail-operations-showcase) · 个人维护

**面向餐饮零售物流的 AI 运营平台工程案例文档**

一个已投产的商业运营平台工程案例文档：整合销售、库存、物流、CRM、HACCP、忠诚度与 POS/秤/ Fiscal 收银集成，AI 部分包括可执行真实操作的助手（含免提语音模式）、行业基准预测、what-if 情景模拟与客户评分。前端 React+Capacitor，后端 Supabase+PostgreSQL，另有本地 Node.js 设备服务器驱动店内硬件。源代码在私有仓库，此仓库仅记录产品工程与系统组织，不提供安装运行方式，不公布性能指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 助手可执行真实操作：建订单、打小票、查仓库，含免提语音模式
- 65 个外部数据集目录与 what-if 情景模拟器
- 订单级渠道分离建模（到店/电话/WhatsApp/外卖等）
- 本地 Node.js/Express 设备服务器经 HTTP REST + UDP 发现驱动店内硬件

## 适用场景

- 了解餐饮零售平台如何把 LLM 接入真实业务操作
- 参考多渠道订单与库存的领域建模方式
- 参考跨模块数据采集支撑预测层的工程做法

## 场景标签

 · 领域:零售/餐饮/物流 运营平台

## 证据(README 行号)

> L4: > channel, inventory, logistics, CRM and an AI assistant that performs real operations.
> L60: An AI assistant that navigates the platform and performs real actions — create orders, print
> L102: - **Operational assistant** — navigates the platform and performs real actions, with a hands-free


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `f405e144df27` · [字段定义](../../DATASET.md)*
