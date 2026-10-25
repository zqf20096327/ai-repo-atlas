# ymm-oss/fsl

⭐ 34 · Rust · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/ymm-oss/fsl) · 组织维护

**面向 LLM 写/验证/修复循环的形式化规约语言与有界模型检查器**

FSL 是一种形式化规约语言，设计目标是由生成式 AI 编写、验证与修复规约。核心工具 fslc 以原生 Rust 可执行文件分发并内置 Z3，执行有界模型检查（BMC）、k 归纳法的无限深度证明及 Z3-free 显式状态引擎，结果以机器可读 JSON 返回以支撑 LLM 循环；另提供从规约生成集成测试脚手架与场景的命令。规约分咨询/需求/设计三层方言，经精化链使需求 ID 在诊断中透传。安装支持脚本、mise 或单文件二进制（含 macOS/Linux/Windows），并附带 Claude Code Agent Skills。仓库内另保留冻结的 Python 兼容参考实现（v2.7.0，非产品本体，未发布到 PyPI）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BMC + k-induction + Z3-free 显式状态三种验证引擎，输出机器可读 JSON
- 单一原生可执行文件分发，Z3 内置，无需 Python 或单独安装求解器
- 三层规约方言经精化链连接，需求 ID 跨诊断透传
- 从规约生成集成测试脚手架（fslc scenarios / testgen）
- 附带 Claude Code Agent Skills（$fsl-requirements / $fsl-business 等）

## 适用场景

- 让 AI 代理编写业务需求规约并自动迭代修复直至无反例
- 对系统规约做有界模型检查与无限深度归纳证明
- 从验收标准生成集成测试脚手架，或对事件日志做一致性检查

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: FSL is a formal specification language for application development, designed with
> L4: the primary goal of being **written, verified, and repaired by generative AI**.
> L9: results as **machine-readable JSON**, for the LLM write → verify → repair loop. It also
> L206: The basic way to use FSL is **not** for a person to memorize the FSL syntax and write it

## 星数曲线

```mermaid
xychart-beta
    title "ymm-oss/fsl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4c42a767f10e` · [字段定义](../../DATASET.md)*
