# sfmqrb/gutcheck

⭐ 14 · Rust · MIT · 推送 2026-09-26 · [GitHub](https://github.com/sfmqrb/gutcheck) · 个人维护

**本地 CPU 语义 grep：用自然语言问题筛选日志、diff 与 JSON 行**

单个 Rust 二进制的命令行工具：对每行、段落、JSON 记录或 diff hunk 提出英文问题（如是否 bug 报告、是否错误日志），通过本地 ONNX 模型打分并保留匹配行。保留 grep 习惯（-n/-v/-r/-C、退出码 0/1/2），提供 -i 实时视图（阈值滑动、重新提问）、--auto 自动阈值、@secret 等命名问题、日志行模糊去重（数字/时间戳/ID 归并以减少模型调用）。首次运行下载 1.3 GB 模型，仅 CPU，无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言问题驱动的 grep 式行筛选，兼容 grep 标志与退出码
- 三个内置模型（multilingual/english/typed），全部本地 CPU 运行
- 日志行形状归并去重，相同形状只调用一次模型（附 Apache/HDFS/Linux 基准）
- --estimate 在执行前预估模型调用次数；每次运行输出调用与耗时回执

## 适用场景

- 在大量日志中按语义筛选错误行而非靠正则匹配
- 在代码库里扫描疑似凭据/PII/安全问题的行
- 对 JSON 记录或 diff hunk 按自然语言条件批量过滤

## 场景标签

`语义搜索` `网络安全` · 领域:知识与检索

## 证据(README 行号)

> L3: **`grep` for meaning.** Ask a plain-English question about every line, paragraph, JSON record or diff hunk, then exp
> L13: The first run downloads a 1.3 GB model to `$XDG_CACHE_HOME/gutcheck`.

## 星数曲线

```mermaid
xychart-beta
    title "sfmqrb/gutcheck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3560a06ffe35` · [字段定义](../../DATASET.md)*
