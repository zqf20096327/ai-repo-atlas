# PriorLabs/tabpfn-client

⭐ 252 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/PriorLabs/tabpfn-client) · [官网](https://www.priorlabs.ai) · 组织维护

**表格基础模型 TabPFN 云端推理 API 的 Python 客户端**

PriorLabs 官方的 tabpfn-client：以 scikit-learn 兼容的 TabPFNClassifier/TabPFNRegressor 接口，通过 token 认证访问 TabPFN 云端服务完成表格数据的分类与回归。fit 与 predict 均在服务器端执行，数据会上传；支持 Thinking Mode（额外 fit 计算换取预测质量，仅 v3 模型）、KV Cache、拟合模型的保存/加载与 submit_fit 后台任务、各阶段耗时报告与回归分布可视化。需注意为云服务，敏感数据不宜上传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- scikit-learn 兼容的 TabPFNClassifier/TabPFNRegressor 云端推理接口
- Thinking Mode 在 fit 阶段探索更多配置并返回调优模型（仅 v3）
- 拟合模型以小型 JSON 记录保存/加载，可跨进程与机器复用
- submit_fit/wait_for_fit 支持后台提交拟合并稍后等待完成

## 适用场景

- 用少量代码对表格数据做分类与回归
- 拟合并缓存一次后反复对同一模型做预测
- 昂贵拟合（Thinking Mode）完成后跨机器加载复用

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L12: TabPFN is a foundation model for tabular data that outperforms traditional methods while being dramatically faster.
> L33: - **TabPFN Client (this repo)**: Easy-to-use API client for cloud-based inference

## 星数曲线

```mermaid
xychart-beta
    title "PriorLabs/tabpfn-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 251 --> 253
    line [252, 252]
```

2026-10-18 252 → 2026-10-25 252（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4f1fb75fc504` · [字段定义](../../DATASET.md)*
