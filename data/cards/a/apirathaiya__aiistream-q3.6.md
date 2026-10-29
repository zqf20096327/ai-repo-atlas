# apirathaiya/aiistream-q3.6

⭐ 17 · Python · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/apirathaiya/aiistream-q3.6) · 个人维护

**在 16GB Mac 上逐字节一致地流式运行 Qwen3.6-35B MoE 的引擎**

面向 Apple Silicon 的专家流式推理引擎（Q3.6 版对应 Qwen3.6-35B-A3B）：约 18GB 专家权重留在内置 SSD，每个 token 只读取被路由选中的专家，并用前瞻读取提前加载；MLX 生成期峰值内存约 1.7GB，实测 15.0 tok/s（16GB M5），输出与未修改 4-bit 模型逐字节一致（相同 token ID 与文本 SHA-256）。提供 OpenAI 兼容 HTTP 服务（含流式与工具调用）及身份校验与基准脚本。限制：仅 MLX/Apple Silicon、单请求串行服务、需约 20GB SSD 空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 专家权重驻留 SSD、按需+前瞻读取，MLX 峰值内存约 1.7GB
- 输出与 stock mlx-lm 运行未修改 checkpoint 逐字节一致，附 verify_identity.py 可复验
- OpenAI 兼容 HTTP 服务，支持流式、工具调用与 seeded sampling
- 内存压力保护：临界时对新请求返回 503，不中断进行中的生成

## 适用场景

- 在 16GB 甚至 8GB 的 Mac 上本地运行未修改的 Qwen3.6-35B-A3B
- 需要可复现输出的评测、回归测试或需匹配参考的 seeded sampling
- 搭建本地私有的 OpenAI 兼容端点（含工具调用）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L32: |Serving|OpenAI-compatible HTTP server on `127.0.0.1`, with streaming and tool calling|
> L6: AiiStream Q3.6 runs a 35-billion-parameter Mixture-of-Experts model on a laptop that cannot hold it in memory:
> L152: - **Other Apple Silicon chips (M1–M4).** The engine uses only standard MLX operations. Byte identity is defined

## 星数曲线

```mermaid
xychart-beta
    title "apirathaiya/aiistream-q3.6 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `92f5262ba013` · [字段定义](../../DATASET.md)*
