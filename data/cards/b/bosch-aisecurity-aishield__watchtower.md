# bosch-aisecurity-aishield/watchtower

⭐ 202 · PureBasic · Apache-2.0 · 推送 2026-03-03 · [GitHub](https://github.com/bosch-aisecurity-aishield/watchtower) · [官网](https://www.boschaishield.com/) · 组织维护

**AI/ML 模型与 Jupyter notebook 的漏洞扫描工具**

Bosch AIShield 开源的安全扫描工具：自动发现仓库中的 AI/ML 模型文件（TensorFlow/Keras/PyTorch/ONNX/GGUF/Scikit-Learn 等格式）与 Jupyter notebook，检测硬编码密钥、PII、过时库、模型反序列化攻击、后门与运行时风险，并按 low/medium/high/critical 四级分类生成三类 JSON 报告。支持从 GitHub、Hugging Face、AWS S3 及本地路径扫描。提供 CLI、Web UI 与 Docker UI 三种运行方式，对齐 OWASP/MITRE/CWE/NIST AI RMF 标准。TF 模型扫描目前仅支持 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动发现并扫描 11 类模型格式与 notebook 文件的漏洞
- 四级风险分类与三类 JSON 报告输出
- 支持 GitHub/Hugging Face/AWS S3/本地文件多来源扫描
- 对齐 OWASP、MITRE、CWE、NIST AI RMF 标准

## 适用场景

- 扫描 Hugging Face 仓库中的模型是否存在后门或反序列化风险
- 检查 notebook 与 Python 文件中的硬编码密钥和 PII 泄露
- 在企业 AI 供应链流程中对模型与代码做安全审计

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L25: **AIShield Watchtower** is designed to automate model and notebook discoveries and conduct comprehensive vulnerabil
> L184: - **Supported Repositories** : AIShield Watchtower supports integration with GitHub, Huggingface and AWS S3 bucket

## 星数曲线

```mermaid
xychart-beta
    title "bosch-aisecurity-aishield/watchtower 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 201 --> 203
    line [202, 202]
```

2026-10-18 202 → 2026-10-22 202（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2b604ea7f335` · [字段定义](../../DATASET.md)*
