# bamler-lab/constriction

⭐ 111 · Rust · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/bamler-lab/constriction) · [官网](https://bamler-lab.github.io/constriction/) · 组织维护

**面向研究与生产的可组合熵编码库（Python/Rust）**

constriction 提供一组可组合的熵编码算法（ANS、Range Coding、实验性 Chain Coding、Huffman），并附带定点算术实现的常用概率分布熵模型及自定义分布适配器。Python API 用于快速原型，Rust API 提供二进制兼容实现，可编译为独立二进制、库或 WebAssembly 模块；Rust 侧支持 no_std。定位包括新型有损/无损压缩方法研究、研究代码到部署软件的迁移，以及数据压缩课程教学素材。MIT/Apache 双许可条款见 README 许可节。

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

- 提供 ANS、Range Coding、Chain Coding、Huffman 四类熵编码器，编码器可互换组合
- Python 与 Rust 提供相似 API 且二进制兼容，Rust 支持 no_std 与 WebAssembly
- 内置定点算术概率分布及自定义分布的可逆量化适配器
- README 附带 300 万符号级基准测试（比特率开销与编解码运行时间）

## 适用场景

- 机器学习压缩方法研究中替换/组合熵编码器（如 bits-back 编码、自回归模型）
- 将 Python 研究原型迁移为 Rust 生产二进制或 WebAssembly 模块
- 数据压缩课程的教学与习题实践

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L10: 1. **to facilitate research on novel lossless and lossy compression methods** by
> L17:  prototypes into standalone binaries, libraries, or WebAssembly modules); and

## 星数曲线

```mermaid
xychart-beta
    title "bamler-lab/constriction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 110 --> 112
    line [111, 111]
```

2026-10-18 111 → 2026-10-23 111（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `fad2b970dc5c` · [字段定义](../../DATASET.md)*
