# CookSleep/LLM_API_Price_Comparator_Web

⭐ 19 · JavaScript · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/CookSleep/LLM_API_Price_Comparator_Web) · [官网](https://cooksleep.github.io/LLM_API_Price_Comparator_Web/) · 个人维护 · 中文 README

**比较各 LLM API 服务商调用同一模型价格的在线工具**

网页版价格计算器：用户输入输入/输出 Token 数量及各服务商的余额、充值金额与调用定价，工具自动获取美元/人民币汇率，计算并按成本从低到高排名，输出人民币与美元费用比较结果；支持表单保存与浏览器历史记录填充。部署方式为 GitHub Pages 静态网站，汇率数据由 GitHub Actions 定时抓取 Alpha Vantage 更新。代码由 Claude 3.5 Sonnet 与 GPT-4o 编写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动获取美元/人民币汇率，比较国内外服务商
- 按成本从低到高的服务商费用排名
- 表单保存与浏览器内历史记录快速填充
- GitHub Actions 定时更新汇率并经 GitHub Pages 部署

## 适用场景

- 选择同一模型在不同 API 服务商下的低价渠道
- 按充值余额和定价估算指定 Token 用量的实际成本
- 自行 Fork 部署一份私有价格比较页面

## 场景标签

 · 领域:LLM 服务选型/成本计算

## 证据(README 行号)

> L5: LLM API Price Comparator Web 是一个在线工具，帮助用户便捷地比较不同LLM API服务商在指定输入输出下调用同一种模型的价格。
> L7: 它会自动获取美元/人民币汇率，允许用户输入服务商的余额、调用定价信息，并计算、比较相对于输入输出Token的成本。

## 星数曲线

```mermaid
xychart-beta
    title "CookSleep/LLM_API_Price_Comparator_Web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `f6ea93cd618b` · [字段定义](../../DATASET.md)*
