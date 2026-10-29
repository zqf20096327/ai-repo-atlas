# PoCInnovation/Infinalys2

⭐ 21 · JavaScript · MIT · 推送 2026-02-13 · [GitHub](https://github.com/PoCInnovation/Infinalys2) · 个人维护

**股票市场多时间尺度价格预测的 Web 应用（PoC）**

基于 Infinalys 项目模型的 PoC：Flask 后端结合深度学习（TensorFlow），读取股票历史与市场指标，生成按日/周/月尺度的价格预测；React 前端展示历史曲线、成交量、技术指标与预测结果，数据经 yahoo-finance-api 抓取。通过 Docker Compose 一键部署，可用 companies.csv 自定义股票池并在 companies_test 中评估。定位为概念验证项目，由三名个人作者维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 深度学习模型基于股票历史与指标生成多时间尺度预测
- React 前端展示历史曲线、成交量与指标
- Docker Compose 一键构建运行（兼容 podman-compose）
- companies.csv 提供 506 家公司列表并可自定义评估股票

## 适用场景

- 在浏览器中查看股票历史行情与模型预测曲线
- 替换 companies_test 中的股票来评估模型表现
- 作为深度学习股票预测的参考实现自行部署试验

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: Infinalys2 is a PoC project which aims to create a stock prediction's app based on Infinalys project's model.
> L7: It's a Web App that displays the history of the stock markets (curve since launch, with stock market indicators, vol

## 星数曲线

```mermaid
xychart-beta
    title "PoCInnovation/Infinalys2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f8045577bdc5` · [字段定义](../../DATASET.md)*
