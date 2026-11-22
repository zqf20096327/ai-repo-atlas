# TransAPI-eng/new-api-model-plaza

⭐ 3 · JavaScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/TransAPI-eng/new-api-model-plaza) · [官网](https://transapi-eng.github.io/new-api-model-plaza/) · 组织维护 · 中文 README

**给 New API / One API 中转站定价页换树状卡片界面的前端组件**

一个 Web Component 形式的前端插件，替换 New API / One API 中转站的 /pricing 模型广场页面：读取站点公开接口的价格与状态数据，按厂商→渠道→模型三层树状卡片展示，计算相对官方价格的折扣、解析动态计费表达式、支持多模型并排对比与模糊搜索；已登录客户可在卡片上一键按分组创建 API Key，管理员可可视化编辑展示配置并导出 JSON 发布。只读公开接口、不改后端，同域部署才支持管理员编辑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 厂商→渠道→模型三层树状卡片，渠道特点自动识别为徽章
- 按官方价、当日汇率与本站充值价计算「比官方省 X%」
- 一键开通 API Key，调用 New API 自带 /api/token 接口
- 单个 plaza.js 零依赖，Web Component + Shadow DOM 样式隔离

## 适用场景

- 中转站站长给自己的 /pricing 页换一套树状卡片界面
- 客户选好分组后一键创建 API Key 并复制接口地址
- 管理员不改计费配置的前提下调整展示层内容

## 场景标签

 · 领域:LLM 基础设施/API 网关配套

## 证据(README 行号)

> L3: **给 New API / One API 中转站的模型广场（/pricing 定价页）换一套好看、好懂的界面。**
> L4: 一行代码接入，只读公开接口，**不改后端、不碰数据库、不影响原站运营**。
> L59: - **隔离**：Web Component + Shadow DOM，样式不会影响原站，原站样式也不会影响它。

## 星数曲线

```mermaid
xychart-beta
    title "TransAPI-eng/new-api-model-plaza 星数(近 2 点)"
    x-axis ["2026-11-12", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-12 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c3268d2072a4` · [字段定义](../../DATASET.md)*
