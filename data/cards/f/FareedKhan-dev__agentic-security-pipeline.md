# FareedKhan-dev/agentic-security-pipeline

⭐ 18 · Jupyter Notebook · MIT · 推送 2026-06-16 · [GitHub](https://github.com/FareedKhan-dev/agentic-security-pipeline) · [官网](https://medium.com/@fareedkhandev/building-an-agentic-security-pipeline-that-finds-proves-and-patches-vulnerabilities-6156aeb4b46f) · 个人维护

**用 7B 开源模型端到端发现、证明并修补 C 内存安全漏洞的流水线**

对 Anthropic 六步 defender's loop 的从零重实现：以 Qwen2.5-Coder-7B-Instruct 在本地 vLLM 上服务，多 agent 并行构造输入引爆 C 程序崩溃，AddressSanitizer 作为真值判定；验证在一次性 Docker 容器中独立重引爆，随后按根因去重、评分并由模型迭代打补丁。全程不调用云端 API。以单个可运行 Jupyter notebook 提供，需 Linux + 单块 NVIDIA GPU + Docker。在埋有 3 个漏洞的 canary 目标上 3/3 发现、证明并修补；对 cJSON 1.7.10 报告 0 个已证明崩溃、4 个 UNPROVEN 候选。README 声明定位为教学/复现而非成品扫描器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六步循环：威胁建模→沙箱→发现→验证→分诊→修补，产出闭环证据
- ASAN 真值 oracle：发现仅在加固容器中真实崩溃才算成立
- vLLM guided_json 结构化输出替代原生工具调用，适配 7B 模型
- 单个 literate notebook 承载全部流程，静态校验脚本无需 GPU

## 适用场景

- 复现/学习 LLM 驱动的漏洞发现与修补闭环
- 在自有 C 服务上运行发现-验证-分诊流程并接入手动审计
- 验证小型开源模型能否胜任多角色 agent 工作流

## 场景标签

`网络安全` `多智能体` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L3: ### An autonomous loop that **finds**, **proves**, and **patches** real C memory-safety vulnerabilities — driven end
> L21: The pipeline targets **C memory-safety bugs** (buffer overflows, use-after-free) compiled with **AddressSanitizer (
> L19: > Anthropic drives the loop with Claude. **We drive the exact same loop with an open-source model**, `Qwen2.5-Coder

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/agentic-security-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `1445c429c1c4` · [字段定义](../../DATASET.md)*
