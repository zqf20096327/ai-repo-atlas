# alexshpunt/explicit-edit-benchmark

⭐ 40 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/alexshpunt/explicit-edit-benchmark) · [官网](https://huggingface.co/spaces/alexshpunt/benchmark-explorer) · 个人维护

**评测编码代理文件编辑精度的开源基准（226 项字节级任务）**

面向编码代理与 agent 框架的文件编辑精度基准：226 个确定性任务（替换/插入/删除/复制/移动/大文件/Unicode 边界），验证器逐字节比对结果。提供 Pi、Codex CLI、OpenCode、GitHub Copilot CLI、DeepSeek Harness 等现成适配器，也可自写适配器；运行后以 PR 形式提交至 Hugging Face Dataset，结果进入公开排行榜并按 harness 家族授予徽章。要求 Linux/WSL2、Node.js 24+、Python 3 与 Bubblewrap。运行在 GitHub Actions 验证路径或本地路径两种方式下，均由一条命令完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 226 个确定性任务，验证器逐字节比对编辑结果
- 内置 9 类 agent CLI 适配器（Pi/Codex CLI/OpenCode/Copilot CLI 等）
- 公开排行榜与 Hugging Face Dataset 存储，按 harness 家族发布徽章
- GitHub Actions 验证运行与本地运行两种提交路径

## 适用场景

- 我开发了新的 agent 编辑工具，想在公开基准上量化它
- 对比不同模型/工具/框架组合对文件编辑的准确率
- 为自己的编码代理项目在 README 中展示基准徽章

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5:  Explicit Edit is an open benchmark for measuring how accurately coding agents and agent harnesses edit files across
> L127: For anything not in this list you write your own adapter. Benchmark automation and public data documents the confi

## 星数曲线

```mermaid
xychart-beta
    title "alexshpunt/explicit-edit-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `66a0d8f4c0d1` · [字段定义](../../DATASET.md)*
