# sangfor-aibuilder/aibuilder-json

⭐ 28 · Python · NOASSERTION · 推送 2026-09-03 · [GitHub](https://github.com/sangfor-aibuilder/aibuilder-json) · [官网]( https://ecnrz718f2z4.feishu.cn/wiki/NE91w0DFfiqgaAkNwQUczefinje?from=from_copylink) · 组织维护 · 中文 README

**将自然语言业务需求转换为 FastGPT 工作流 JSON 的技能包**

由深信服（Sangfor）AIBuilder 团队开发的 skill 包：把自然语言描述的业务流程转换为可直接导入 FastGPT 的工作流 JSON 配置，生成过程包含假设确认、节点/边/配置生成、契约验证与文件保存。输出自动附带错误处理路径、用户指导文本与中文界面标签，支持 15 类 FastGPT 节点。以 SKILL.md 形式安装到 Claude Code、OpenClaw、Costrict.ai、Trae 等支持 skills 的平台；另附纯标准库的 Python 脚本用于 JSON 验证与模板检查。属深信服 AIBuilder（基于 FastGPT 的企业 RAG 平台）生态的一部分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成含节点、边、配置的完整 FastGPT 工作流 JSON
- 内置验证：节点 IO 完整性、边连接性、引用有效性、分支句柄、布局间距
- 支持 15 类节点：输入收集、知识检索、分类、分支、循环、HTTP 请求等
- 附带零第三方依赖的 Python 验证/检查脚本（Python 3.9+ 标准库）

## 适用场景

- 用对话方式生成 HR 简历筛选、工单分类等 FastGPT 工作流
- 为 RAG 文档问答场景搭建含知识库检索节点的工作流
- 导入前用脚本验证 FastGPT JSON 是否符合运行时契约

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L13: AIBuilder JSON Creator is a professional tool that transforms natural-language business requirements into productio
> L39: This tool works with **any AI agent platform that supports skills**, including:

## 星数曲线

```mermaid
xychart-beta
    title "sangfor-aibuilder/aibuilder-json 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c15a42571afe` · [字段定义](../../DATASET.md)*
