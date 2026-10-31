# microsoft/llm-42

⭐ 33 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/microsoft/llm-42) · [官网](https://www.arxiv.org/pdf/2601.17768) · 组织维护

**为 SGLang 增加可验证确定性的 LLM 推理系统（decode–verify–rollback）**

构建于 SGLang v0.5.3 之上的推理确定性层：在动态批处理下用未修改 GPU kernel 正常解码，定期以固定形状调度重放一段 token 窗口校验一致性，不一致则回滚到最近已验证位置；仅标记 is_deterministic=True 的请求进入校验路径，其余请求按原速运行。提供 Docker 启动脚本与多个配置项（窗口大小、验证批大小等）。论文被 SOSP 2026 接收，作者来自微软研究院与华盛顿大学。硬件要求为 4× H100 PCIe 等配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- decode–verify–rollback 协议实现确定性 LLM 推理，无需改写 GPU kernel
- 仅确定性请求承担校验开销，其余请求全速运行
- 构建于 SGLang v0.5.3，通过 --enable-llm42 等参数启用
- SOSP 2026 论文配套 artifact（sosp-artifact/ 目录）

## 适用场景

- 需要跨运行可复现输出的 LLM 服务部署
- 对推理结果一致性有审计要求的场景
- 研究动态批处理下确定性推理的性能表现

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L16: **LLM-42** enables deterministic LLM inference via a **decode–verify–rollback** protocol, without rewriting GPU ker
> L20: Standard LLM serving is non-deterministic: dynamic batching changes GPU reduction orders, producing different outpu

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/llm-42 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-31 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3baec0954f3e` · [字段定义](../../DATASET.md)*
