# george1-adel/ReconFusionAi

⭐ 16 · Python · 推送 2026-07-12 · [GitHub](https://github.com/george1-adel/ReconFusionAi) · 个人维护

**面向安全人员的本地 AI 密钥/PII 扫描器，用上下文过滤误报**

Web 资产安全侦察工具：以 1,183+ 条正则模式检测暴露的密钥、凭据、PII 与漏洞线索，再通过本地 Ollama（默认 qwen2.5:1.5b）做上下文推理评分，过滤示例代码等误报。支持 SQLite AI 缓存、LRU 去重、CPU/GPU 温控与请求节流，输出 findings.json 与 discoveries.json。需 Python 3.8+ 与已运行的 Ollama，面向授权测试的安全专业人员，全部处理在本地进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,183+ 检测模式（Gitleaks 199+、密钥库 803+、PII 97+、关键发现 84）
- Ollama 本地模型（默认 qwen2.5:1.5b）做上下文融合评分与误报过滤
- SQLite AI 缓存（1h TTL）与 LRU 内存缓存减少重复调用
- 硬件监控自动降温与请求节流，输出 findings/discoveries 双报告

## 适用场景

- 授权渗透测试与 bug bounty 中扫描 Web 资产泄露的密钥与凭据
- 大批量 URL 扫描时过滤测试数据造成的误报
- 本地离线扫描敏感目标，数据不出内网

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: ReconFusionAI is an advanced security reconnaissance tool that combines massive regex pattern libraries with AI cont
> L19: - **Ollama Integration**: Uses `qwen2.5:1.5b` (or custom models) for reasoning.
> L111: - **100% Local Processing**: AI analysis runs on your machine via Ollama. No data leaves your network.

## 星数曲线

```mermaid
xychart-beta
    title "george1-adel/ReconFusionAi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a0461d2f6915` · [字段定义](../../DATASET.md)*
