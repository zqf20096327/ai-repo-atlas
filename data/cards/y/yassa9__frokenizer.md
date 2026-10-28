# yassa9/frokenizer

⭐ 24 · C++ · MIT · 推送 2026-04-03 · [GitHub](https://github.com/yassa9/frokenizer) · 个人维护

**面向 Qwen 的零分配头文件 C++ BPE 分词器**

单头文件 C++17 库，将 Qwen 分词器的词表与合并规则在编译期烧录为静态常量，用 re2c 把 Qwen 正则编译为 DFA 状态机消除回溯，热路径禁用 malloc/new/std::string 等堆操作，输出由调用方预分配缓冲区承载。提供 encode/decode API 与 OpenMP 批量示例，附带与 tiktoken 逐字节一致性校验、内存安全测试与 libFuzzer 模糊测试。限定为静态硬编码的 Qwen 分词器，多语言文本吞吐会下降。面向推理服务器、边缘与嵌入式开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编译期 re2c DFA 消除正则回溯，词表烧录为静态常量
- 热路径零堆分配，调用方预分配缓冲区输出 uint32 token id
- 无全局可变状态，可直接放入 OpenMP/std::thread 线程池
- 提供 tiktoken 逐字节一致性校验、ASan/UBSan 安全测试与 libFuzzer 模糊测试

## 适用场景

- 为 Qwen 推理服务器替换运行时分词器以降低延迟抖动
- 在无堆环境的嵌入式/边缘设备上做 BPE 分词
- 多线程批量 tokenize 高吞吐预处理文本

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L20: Frokenizer 🥶 or [Frozen Tokenizer] is a suckless, zero allocation, zero dependency, header-only c++ BPE inference t
> L67: # Usage
> L246: - `C++17` compiler (`gcc` or `clang`) with `openmp` support.

## 星数曲线

```mermaid
xychart-beta
    title "yassa9/frokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b1f5d70c4a24` · [字段定义](../../DATASET.md)*
