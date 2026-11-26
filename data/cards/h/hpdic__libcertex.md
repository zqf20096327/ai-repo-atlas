# hpdic/libcertex

⭐ 5 · Cuda · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/hpdic/libcertex) · [官网](https://arxiv.org/abs/2611.29252) · 个人维护

**NVIDIA GPU 上的精确 k 近邻搜索库，兼容 cuVS/Faiss 等接口**

开源实现 CertEx（认证排除）机制的 CUDA C++ 库，附带 Python/C/C++ 绑定：用张量核上的半精度下界筛选排除绝大多数候选，仅对幸存者做双精度精确验证，结果与穷举搜索一致，不提供精度换速度的选项。支持 L2、余弦、内积度量、按标签过滤搜索及主机内存存储超大集合，支持运行中增删向量。以 cuVS 模块形式组织，保留被替换库的调用接口，迁移仅需改 import。要求 Linux、Python ≥3.11、CUDA 12 及计算能力 ≥8.0 的 NVIDIA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结果与双精度穷举搜索一致，无 recall/精度参数
- 提供 cuVS（C++/C/Python）、Faiss、torch.topk、FlashInfer 稀疏注意力的 drop-in 接口
- 支持 Euclidean/余弦/内积度量与标签过滤搜索
- 支持主机内存存储与运行中动态增删向量

## 适用场景

- 为评估近似索引生成精确 ground truth
- 以精确 top-k 键替代 torch.topk/FlashInfer 实现稀疏注意力
- 构建精确 k-NN 图并做近重复去除
- 数据集超出显存时用主机内存做精确向量检索

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L9: certex is the open-source implementation of CertEx (Certified Exclusion), exact k-nearest-neighbor search on NVIDIA
> L20: it is a drop-in for cuVS (C++, C, and Python), Faiss, `torch.topk`, and the sparse-attention top-k of FlashInfer.
> L26: pip install certex            # Linux, Python >= 3.11, CUDA 12, an NVIDIA GPU of compute capability >= 8.0


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `06a2dd0bd8c6` · [字段定义](../../DATASET.md)*
