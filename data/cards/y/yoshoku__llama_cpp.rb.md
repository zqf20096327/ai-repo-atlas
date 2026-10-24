# yoshoku/llama_cpp.rb

⭐ 236 · C · MIT · 推送 2026-09-04 · [GitHub](https://github.com/yoshoku/llama_cpp.rb) · [官网](https://rubygems.org/gems/llama_cpp) · 个人维护

**llama.cpp 的 Ruby 绑定，供 Ruby 应用加载量化模型生成文本**

以原生扩展形式为 llama.cpp 提供 Ruby 绑定，使 Ruby 程序可加载 GGML/GGUF 量化模型并执行文本生成。安装需先安装 llama.cpp（README 给出 homebrew 命令），再通过 gem 或 bundler 安装，需指定 homebrew opt 目录。使用时参照 llama.cpp README 准备量化模型（如 open_llama_7b、tiny_llama_1b），README 附 Ruby 生成示例代码。README 同时提示另一个基于 FFI 的 Ruby 绑定 rllama 作为高阶 API 选择。MIT 许可。

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

- 为 llama.cpp 提供 Ruby 原生扩展绑定
- 支持加载量化模型（open_llama_7b、tiny_llama_1b 等）并用 Ruby 代码生成文本
- 提供 gem/bundler 安装方式与 homebrew 安装 llama.cpp 的前置步骤

## 适用场景

- 在 Ruby 应用中本地运行 LLM 推理
- 通过 Ruby API 加载 GGUF 量化模型生成文本

## 场景标签

 · 领域:LLM 基础设施

## 证据(README 行号)

> L7: llama_cpp.rb provides Ruby bindings for the llama.cpp.
> L48: An example of Ruby code that generates sentences with the quantization model is as follows:

## 星数曲线

```mermaid
xychart-beta
    title "yoshoku/llama_cpp.rb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 235 --> 237
    line [236, 236]
```

2026-10-18 236 → 2026-10-24 236（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `51b8070c02bb` · [字段定义](../../DATASET.md)*
