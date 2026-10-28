# almide/almide

⭐ 35 · Rust · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/almide/almide) · [官网](https://almide.github.io/docs/) · 组织维护

**面向 LLM 代码生成的静态类型语言，错误诊断直接给出修复**

一种静态类型编程语言，定位为 AI 编写和编辑代码的目标语言：当模型出错时编译器在编写期报错并给出具体修复（含位置与修复建议）。单一源码可编译为原生二进制（经 Rust）与 WebAssembly（直接发射，不依赖 LLVM），承诺契约行为上字节一致的输出；`almide verify` 校验所有权、命名与能力见证。提供安装脚本、浏览器 Playground 与从源码构建（需 Rust 1.96+）。项目处 pre-1.0 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 编译到原生二进制与 WebAssembly，契约行为上字节一致
- 诊断信息附带具体修复建议，供模型下一轮修正
- 显式效果系统（effect fn / expr!），无 GC 无生命周期注解的所有权推断
- 内置 `almide test/fmt/check/verify` 工具链

## 适用场景

- 让 LLM 生成/修改代码时由编译器即时拦截错误并指明修复
- 同一份源码编译到原生与 wasm 双目标
- 为 AI agent 提供可验证的编程语言运行环境

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L21: Almide is a statically-typed language for code that AI writes and edits. The claim is not that the model gets it ri
> L3:  When the model is wrong, the compiler names the fix.

## 星数曲线

```mermaid
xychart-beta
    title "almide/almide 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0034a89d149c` · [字段定义](../../DATASET.md)*
