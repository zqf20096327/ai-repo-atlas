# AnonKryptiQuz/XSSGAI

⭐ 44 · Jupyter Notebook · MIT · 推送 2026-02-04 · [GitHub](https://github.com/AnonKryptiQuz/XSSGAI) · [官网](https://AnonKryptiQuz.github.io/) · 个人维护

**给安全研究者的 AI XSS payload 生成器**

基于 PyTorch 的 XSS 攻击载荷生成工具：以 6 层 Transformer Encoder 从真实攻击数据集学习模式，配合 Top-P 采样、多轴均衡与编码增强生成载荷，并内置新颖性检测与 HTML 结构校正层。通过 Jupyter Notebook（含 IPyWidgets 交互界面）运行，可本地安装或上传至 Google Colab 执行；提供预训练权重跳过约 60 分钟训练。面向安全研究人员与道德渗透测试者，需 Python 3.10+ 与 CUDA GPU（推荐 Tesla T4 及以上），Colab 路径可免除本地硬件要求。声明仅限教育、安全研究与授权测试用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 层 Transformer Encoder 生成 XSS 载荷，支持 384 token 序列
- Top-P 采样与多轴均衡，兼顾常见与罕见高价值标签
- 集合式新颖性检测区分‘记忆型’与‘新颖’载荷
- 预训练权重可跳过训练，支持 Google Colab 云端运行

## 适用场景

- 渗透测试中生成多样化 XSS 载荷以发现漏洞
- 安全研究中验证 WAF 对编码混淆载荷的拦截能力
- 无本地 GPU 时在 Colab 上运行实验

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **XSSGAI** is the **first-ever AI-powered XSS (Cross-Site Scripting) payload generator**. Leveraging machine learnin
> L5: **XSSGAI v2.0** is the evolution of the first-ever AI-powered XSS payload generator. Moving away from traditional RN
> L31: |**Model Type**|Transformer Encoder (Generative)|

## 星数曲线

```mermaid
xychart-beta
    title "AnonKryptiQuz/XSSGAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c596614c57c6` · [字段定义](../../DATASET.md)*
