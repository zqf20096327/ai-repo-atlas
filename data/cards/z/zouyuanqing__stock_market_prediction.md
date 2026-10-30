# zouyuanqing/stock_market_prediction

⭐ 36 · TypeScript · MIT · 推送 2026-08-02 · [GitHub](https://github.com/zouyuanqing/stock_market_prediction) · 个人维护 · 中文 README

**桌面股票预测工具：ARIMA/LSTM 预测行情并用 LLM 生成分析**

基于 Tauri 2.0 + React 18 + TypeScript 的股票市场预测桌面应用：从 Yahoo Finance、Stooq 获取股票数据，计算 MA/RSI/MACD 等技术指标并生成交易信号；预测部分通过 Python Sidecar 运行 ARIMA（pmdarima 自动定阶）与 2 层 PyTorch LSTM（未来 5 日滚动预测）。AI 深度分析支持 DeepSeek、OpenAI 及兼容 API，填入 Key 后自动拉取模型列表，不填则跳过 AI 分析仅显示技术指标。网页版为模拟数据演示模式。面向需要进行股票行情分析与预测的个人用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ARIMA + PyTorch LSTM（2 层）双模型预测，未来 5 日多步滚动
- Rust 通过 Python Sidecar 以 stdin/stdout JSON 调用预测脚本
- 兼容 OpenAI API 格式的多家服务（DeepSeek/月之暗面/智谱等），自动发现模型
- Yahoo Finance 与 Stooq 双数据源一键切换

## 适用场景

- 查询股票并查看技术指标、交易信号与价格图表
- 运行 ARIMA/LSTM 模型获取未来 5 日预测
- 配置 API Key 后生成 AI 深度分析报告

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: 基于 **Tauri 2.0 + React 18 + TypeScript** 构建的现代化股票市场预测工具，集成 AI 智能分析。
> L68: ARIMA 和 LSTM 预测使用 Python Sidecar 模式：
> L72: - PyTorch LSTM 模型（2 层），支持未来 5 日多步滚动预测

## 星数曲线

```mermaid
xychart-beta
    title "zouyuanqing/stock_market_prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `86fc3d7b316b` · [字段定义](../../DATASET.md)*
