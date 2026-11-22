# dongdonga11/dsh-customer-service

⭐ 3 · JavaScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/dongdonga11/dsh-customer-service) · [官网](https://github.com/dongdonga11/dsh-customer-service) · 个人维护 · 中文 README

**给电商卖家的多平台 AI 客服插件：AI 回复带闸门与审计**

DSH 插件形态的客服工作台：Chrome MV3 扩展接管已登录的闲鱼/抖音页面，通过本地 WebSocket 桥（127.0.0.1 端口）收发消息，统一到「平台→账号卡→工作台」界面。AI 自动回复默认关闭，开启后经 9 道闸门（红线、结构化输出、回读校验、审计等）约束，并只依据本地 Markdown 资料库（关键词检索）回答。数据全部落在本地，支持人工随时接管与 AI 沙箱测试。需先运行 DeepSeek Harness，README 提示该适配形态可能违反平台用户协议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 道闸门约束 AI 自动回复，每次回复记录依据资料与闸门判定
- 本地资料库：AGENTS.md 规则优先读取，AI 只依据已写入资料回答
- Chrome 扩展不碰登录、不存 cookie，数据只落本地
- 支持闲鱼/抖音（含抖音来客）双平台多账号接入

## 适用场景

- 闲鱼/抖音店铺把多个后台消息统一到一个工作台处理
- 让 AI 按自有产品资料生成回复，人工随时接管
- 付款后自动交付网盘链接等闲鱼运营流程

## 场景标签

`聊天机器人` `文档问答` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: > 给 **DeepSeek Harness (DSH)** 用的**多平台 AI 客服工作台插件**：
> L44: - **9 道闸门**：默认关 / 幂等 / 人工优先 / 静默期 / 最小间隔 / 红线 / 结构化输出 / 回读校验 / 审计

## 星数曲线

```mermaid
xychart-beta
    title "dongdonga11/dsh-customer-service 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-21 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c9f14ab93cd3` · [字段定义](../../DATASET.md)*
