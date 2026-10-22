# open-ribbi/velocut

⭐ 455 · TypeScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/open-ribbi/velocut) · [官网](https://ribbi.ai) · 组织维护 · 中文 README

**浏览器内本地优先的 AI 视频编辑与 3D 场景制作工具**

由 Ribbi 开发的浏览器端视频编辑器与 3D 导演工具：多轨剪辑、字幕/动效、WebCodecs 导出 MP4、WebGPU 合成，项目数据存于浏览器 IndexedDB/OPFS。人与 Codex 等 LLM agent 通过同一 JSON 命令协议和 MCP 服务操作同一项目文档与撤销历史，agent 可创建场景、导入 GLB、控制相机并做视觉检查；另支持配置自定义视频/语音/音乐生成模型。手动剪辑无需模型 API key；需要 Node.js 22.6+ 与支持 WebGPU/WebCodecs 的 Chrome/Edge。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轨视频剪辑 + 可编辑 3D Director，人与 LLM agent 共用同一命令协议与分支历史
- MCP 服务供 Codex 及其他客户端接入，插件自动启动预构建 Studio
- 声明式配置自定义视频/语音/音乐生成模型（YAML/JSON 定义，Base URL + Token）
- 本地优先：媒体存储与渲染留在浏览器，WebCodecs 编码导出 MP4

## 适用场景

- 在浏览器本地剪辑视频、搭建字幕与动效，不依赖云端存储
- 通过 Codex 等 agent 用自然语言搭建 3D 场景并编排镜头
- 接入自有视频生成渠道，把生成结果作为素材放入时间线

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L14: Velocut combines a multitrack video editor, an editable 3D Director and a programmable project runtime. Arrange a s
> L42: - Manual editing and the Codex integration need no additional model API key.
> L64: The model runs in Codex. The plugin supplies tools for scene creation, object editing, GLB import, arrangement, cam

## 星数曲线

```mermaid
xychart-beta
    title "open-ribbi/velocut 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 454 --> 456
    line [455, 455]
```

2026-10-18 455 → 2026-10-22 455（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6f2666f71061` · [字段定义](../../DATASET.md)*
