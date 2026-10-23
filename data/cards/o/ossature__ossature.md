# ossature/ossature

⭐ 202 · Python · MIT · 推送 2026-08-07 · [GitHub](https://github.com/ossature/ossature) · [官网](https://ossature.dev) · 组织维护

**规格驱动的构建系统：用 LLM 把规格说明编译成可运行代码**

开发者以 SMD 规格（需求/验收标准）、AMD 架构、VMD 验证用例三种文件描述软件，Ossature 通过 validate（纯结构校验）、audit（LLM 审读规格并生成可编辑的构建计划）、build（逐任务生成代码、运行验证命令、失败进入修复循环）三个命令完成从规格到代码的构建。构建为增量式，改动一个规格仅重建受影响任务；VMD 用例中期望值不暴露给 LLM，代码须实际通过测试。支持 Anthropic/OpenAI/Mistral/Google 等托管服务及 Ollama 本地模型。当前 0.x 版本，API 与格式不稳定。需 Python 3.14+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SMD/AMD/VMD 三种规格文件驱动的增量构建流程
- validate/audit/build 三命令工作流，audit 计划可人工审阅编辑
- VMD 测试的期望值对 LLM 不可见，防止代码针对测试编写
- 失败任务进入修复循环，支持 review 模式对照契约检查生成代码

## 适用场景

- 以规格为单一事实来源生成并维护项目代码
- 需求变更后编辑规格、仅重建受影响的任务
- 在本地 Ollama 或多家托管 LLM 之间切换生成后端

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L15: An open-source build system that turns specs into working code.
> L35: - `ossature build` runs the plan task by task. Each task generates a few files, runs its verify command, and on fai

## 星数曲线

```mermaid
xychart-beta
    title "ossature/ossature 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 201 --> 203
    line [202, 202]
```

2026-10-18 202 → 2026-10-23 202（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `13e399509021` · [字段定义](../../DATASET.md)*
