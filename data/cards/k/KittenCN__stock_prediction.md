# KittenCN/stock_prediction

⭐ 385 · Python · GPL-3.0 · 推送 2026-09-28 · [GitHub](https://github.com/KittenCN/stock_prediction) · [官网](https://www.coderfan.com) · 个人维护 · 中文 README

**基于 PyTorch 的股票时间序列预测实验项目**

基于 PyTorch 的股票预测实验代码库：通过 akshare 等接口获取行情数据，经预处理后训练与推理，支持 LSTM、Transformer、Hybrid、PTFT/VSSM、Diffusion、Graph 等 11 种模型结构，并提供单元测试、make/CI 质量入口与配置文件。面向量化研究开发者，以源码脚本形式运行。README 明确声明输出仅供研究、不构成投资建议，数据接口可能因上游变化失效，模型效果需在独立样本与真实交易成本下验证。采用 GPL-3.0 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 11 种模型结构（lstm/transformer/hybrid/ptft_vssm/diffusion/graph 等）
- 含行情获取、预处理、训练、推理、评估的完整脚本链路
- 提供 pytest 单元测试与 make test/make ci 质量入口

## 适用场景

- 研究神经网络结构在股票时间序列预测上的表现
- 获取行情数据并搭建训练/推理实验流水线
- 作为时序预测实验代码基础进行扩展与复现

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: 基于 PyTorch 的股票时间序列预测实验项目，包含行情获取、特征处理、训练、推理和模型评估。代码支持 LSTM、Transformer、Hybrid、PTFT/VSSM、Diffusion 和 Graph 等实验模型。预测输出仅
> L36: `--model` 支持 `lstm`、`attention_lstm`、`bilstm`、`tcn`、`multibranch`、`transformer`、`cnnlstm`、`hybrid`、`ptft_vssm`、`dif

## 星数曲线

```mermaid
xychart-beta
    title "KittenCN/stock_prediction 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 382 --> 386
    line [383, 385, 385]
```

2026-10-18 383 → 2026-10-23 385（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `42e560987d03` · [字段定义](../../DATASET.md)*
