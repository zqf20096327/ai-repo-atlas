# yuniko-software/bge-m3-onnx

⭐ 45 · Jupyter Notebook · Apache-2.0 · 推送 2026-05-18 · [GitHub](https://github.com/yuniko-software/bge-m3-onnx) · 组织维护

**BGE-M3 多语言嵌入模型的 ONNX 多语言实现（C#/Java/Python）**

将 BGE-M3 嵌入模型与 XLM-RoBERTa 分词器转换为 ONNX 格式，并提供 C#、Java、Python 三种本地实现，可生成 dense、sparse 与 ColBERT 三种向量。仓库含转换用 Jupyter notebook、跨语言一致性测试脚本与参考嵌入生成脚本；模型可从 releases 下载或自行用 notebook 转换。支持 CPU 与 CUDA GPU 加速（C#/Java 需另行安装 CUDA 和 cuDNN），本地运行无需联网。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 BGE-M3 全部三种嵌入：dense、sparse、ColBERT
- C#/Java/Python 跨平台本地实现，离线运行
- 提供 FlagEmbedding→ONNX 转换 notebook 与跨语言一致性测试脚本
- 支持 CUDA GPU 加速（Python 可经 onnxruntime-gpu 包，C#/Java 需单独装 CUDA/cuDNN）

## 适用场景

- 在不依赖 Python/PyTorch 的 C# 或 Java 服务中本地生成 BGE-M3 嵌入
- 构建需要多向量（dense+sparse+ColBERT）检索的本地嵌入管线
- 验证多语言实现产生的嵌入与 Python 参考结果一致

## 场景标签

 · 领域:机器学习/嵌入模型

## 证据(README 行号)

> L13: This repository demonstrates how to convert the complete BGE-M3 model to ONNX format and use it in multiple program
> L19: - Generate all three BGE-M3 embedding types: dense, sparse, and ColBERT vectors

## 星数曲线

```mermaid
xychart-beta
    title "yuniko-software/bge-m3-onnx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a8bb1fbf943e` · [字段定义](../../DATASET.md)*
