# 5ak3t/ej

⭐ 5 · Python · GPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/5ak3t/ej) · [官网](https://huggingface.co/5ak3t/ej) · 个人维护

**给开发者的 11 MB CPU 小模型：文本分类决策并输出校准概率**

ej 是一个 CPU 推理的分类决策模型与配套 Python 包：输入自由文本或 JSON 状态加一组类型化问题（choice/noul/score），每次调用输出每题的概率分布，推理过程不调用 LLM。模型为单文件 model.ejpack（约 11.4 MB，含 tokenizer 与编码器配置），加载前逐节做 sha256 校验，基于 e5-small-v2 编码器。支持少样本 adapt 适配与从标注数据自行训练；README 明确未见工作流准确率低（.419）且仅支持英文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次调用回答 choice/noul/score 三类问题并输出概率分布
- 单文件 11.4 MB 权重，加载前逐节 sha256 校验，CPU 推理、固定线程数下确定性
- 支持少样本 adapt 适配与 python -m ej.train 自训练
- 校准质量按 suite 用 ECE 度量，基准结果附 95% 置信区间

## 适用场景

- 把支持工单路由到计费、退货或技术支持团队并给出概率
- 在边缘/无 GPU 环境做文本是/否判断与评分
- 用少量标注记录把模型适配到自己的工作流

## 场景标签

 · 领域:机器学习/文本分类

## 证据(README 行号)

> L24: You give ej a `state` (free text, or a JSON object as text) and a set of typed questions; it returns one probabilit
> L25: distribution per question. There is no LLM at inference. This repository holds the package, the training and evalua
> L36:  tokenizer and the encoder config are inside it, no base model is fetched. CPU only, deterministic for a fixed thre

## 星数曲线

```mermaid
xychart-beta
    title "5ak3t/ej 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-20 5 → 2026-11-22 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `616771bdb33f` · [字段定义](../../DATASET.md)*
