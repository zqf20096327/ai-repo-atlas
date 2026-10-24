# Dicklesworthstone/acip

⭐ 331 · Shell · NOASSERTION · 推送 2026-09-21 · [GitHub](https://github.com/Dicklesworthstone/acip) · 个人维护

**给 LLM 部署者的提示注入防御提示框架（可直接加入系统提示）**

以版本化 Markdown 文件形式提供的提示工程防御框架（v1.0/1.2/1.3），通过前置注入一段指令与示例构成的 '认知接种' 提示，引导模型识别并拒绝提示注入攻击（含 RAG/工具间接注入、多轮聚合、隐蔽通道外泄等）。v1.3 增加可选审计模式（ACIP_AUDIT_MODE）、六个高风险领域的三级处置规则、八个术语定义与逐级升级拒绝策略。使用方式为 git clone 后将提示全文置于每次 LLM 交互开头，或用于独立检查模型层。README 明确声明不提供完美保护，且会增加 token 用量与时延。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个版本化提示文件，v1.3 为推荐生产版本（约 3,200 token）
- v1.3 可选审计模式输出机器可解析拒绝标签（ACIP_AUDIT_MODE=ENABLED）
- 六个高风险领域的 Allowed/Sensitive-Allowed/Disallowed 三级处置规则
- 会话内逐级升级拒绝策略（3 次拒绝后切换最小化拒绝）

## 适用场景

- 在带工具或 RAG 的 LLM 生产部署中前置防御提示注入
- 用独立 checker 模型对用户输入做注入筛查
- 在安全监控工作流中开启审计模式收集拒绝信号

## 场景标签

`提示工程` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L12: The **Advanced Cognitive Inoculation Prompt (ACIP)** is a carefully engineered framework designed to significantly 
> L67: This structure enables easy integration into existing LLM deployment workflows, either by directly including the AC
> L83: ## Integration Approaches

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/acip 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 330 --> 333
    line [332, 331, 331]
```

2026-10-18 332 → 2026-10-24 331（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `afaf15e13887` · [字段定义](../../DATASET.md)*
