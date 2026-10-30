# porespellar/Zer0Fit

⭐ 32 · Python · Apache-2.0 · 推送 2026-09-04 · [GitHub](https://github.com/porespellar/Zer0Fit) · 个人维护

**通过 MCP 向 AI 助手开放时序预测与表格分类/回归模型的工具服务器**

基于 Model Context Protocol（SSE/Streamable HTTP）的 MCP 工具服务器，将 Google TimesFM 3.0（时序预测）与 TabFM v1.0.0（表格分类/回归）基础模型以 4 个工具（inspect/upload/forecast/tabular）暴露给聊天客户端（主要适配 Open WebUI），零样本无需训练。提供文件上传与自动检查、预计算指标（accuracy/F1/R² 等）、TTL 模型卸载与互斥 VRAM 管理。通过 install.sh 一键构建 Docker 部署，需 NVIDIA GPU（16GB VRAM）、32GB RAM 与 40GB 磁盘；声明仅供研究与教育用途，TabFM 权重非商业。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个 MCP 工具：zer0fit_inspect / zer0fit_upload_csv / zer0fit_forecast / zer0fit_tabular
- 零样本预测：无需训练、超参调优或特征工程
- 预测附带预计算指标（分类：accuracy/per-class F1/混淆矩阵；回归：R²/MAE/RMSE/MAPE）
- TTL 自动卸载与单模型热加载的 VRAM 管理，支持 ARM64 与 x86_64

## 适用场景

- 在聊天中附加 CSV 并用自然语言请求预测，无需 ML 专业知识
- 为 Open WebUI 等 MCP 客户端接入时序预测与表格分类/回归能力
- 在 GPU 服务器上以 Docker 一键部署零样本预测工具服务

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Zer0Fit exposes Google's **TimesFM 3.0** (time-series forecasting) and **TabFM v1.0.0** (tabular classification/regr
> L9:  Zer0Fit tools in Open WebUI — zer0fit_inspect, zer0fit_forecast, and zer0fit_tabular discovered as MCP tools
> L238: Zer0Fit speaks standard MCP over SSE and Streamable HTTP. The following clients have been tested and verified:

## 星数曲线

```mermaid
xychart-beta
    title "porespellar/Zer0Fit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8f8b913b7a50` · [字段定义](../../DATASET.md)*
