# geniusrise/geniusrise

⭐ 62 · Go · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/geniusrise/geniusrise) · [官网](https://geniusrise.ai/) · 组织维护

**在自有基础设施上部署 LLM/STT/TTS 的运维框架**

单二进制加一个 YAML 文件的自托管方案：读取 deploy.yaml 声明模型与预算，生成 OpenAI 兼容 HTTPS 端点（chat/transcriptions/speech），底层按模型选用 vLLM、llama.cpp、speaches 等运行时，支持自动缩容到零与月度预算上限、按 key 限流。节点零入站端口、经 mTLS 拨入网关，适配 NAT/防火墙环境。部署目标覆盖 AWS、SSH 裸金属/家庭实验室及 GCP/Azure/RunPod 等云，不依赖 Kubernetes。面向希望在自己云上运行开源模型的开发者/团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容端点（/v1/chat/completions、/v1/audio/*）
- 按模型选配优化运行时（vLLM、llama.cpp、speaches）
- scale-to-zero 自动缩容与硬性月预算上限、按 key 限流
- 节点零入站端口、mTLS 拨入网关，可部署于 NAT/防火墙后

## 适用场景

- 在自有云或家庭实验室上托管开源 LLM 并暴露 OpenAI 兼容 API
- 按预算上限自动伸缩推理服务并缩容到零
- 通过单个 YAML 管理多模型部署与限流

## 场景标签

`推理引擎` `MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: **Run open LLM, STT and TTS models on your own infrastructure, in the simplest way possible.**
> L17: - tested, optimized runtimes per model (vLLM, llama.cpp, speaches)

## 星数曲线

```mermaid
xychart-beta
    title "geniusrise/geniusrise 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-31 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e286e482a509` · [字段定义](../../DATASET.md)*
